# src/parser.py
from typing import List, Optional
from dataclasses import dataclass

@dataclass
class AST:
    type: str
    value: str = ""
    children: List['AST'] = None
    
    def __post_init__(self):
        if self.children is None:
            self.children = []

class Parser:
    def __init__(self, tokens: List[tuple]):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[0] if tokens else None
    
    def eat(self, token_type: str = None, value: str = None) -> tuple:
        if not self.current_token:
            raise SyntaxError("Unexpected end of input")
        
        if token_type and self.current_token[0] != token_type:
            raise SyntaxError(f"Expected {token_type}, got {self.current_token[0]}")
        
        if value and self.current_token[1] != value:
            raise SyntaxError(f"Expected '{value}', got '{self.current_token[1]}'")
        
        token = self.current_token
        self.pos += 1
        self.current_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None
        return token

    def peek(self) -> Optional[tuple]:
        return self.current_token

    def parse(self) -> AST:
        statements = []
        
        while self.current_token:
            try:
                if self.current_token[0] == 'FUNC':
                    stmt = self.parse_function()
                elif self.current_token[0] == 'PRINT':
                    stmt = self.parse_print()
                elif self.current_token[0] == 'TYPE':
                    stmt = self.parse_var_decl()
                elif self.current_token[0] == 'IDENT':
                    next_token = self.tokens[self.pos + 1] if self.pos + 1 < len(self.tokens) else None
                    if next_token and next_token[1] == '(':
                        stmt = self.parse_function_call()
                    elif next_token and next_token[0] == 'ASSIGN':
                        stmt = self.parse_assignment()
                    else:
                        self.eat()
                        continue
                else:
                    self.eat()
                    continue
                
                if stmt:
                    statements.append(stmt)
                    
            except Exception as e:
                print(f"Parser error: {e}")
                # Skip to next potential statement
                self.pos += 1
                self.current_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None
        
        return AST('Program', children=statements)
    
    def parse_function(self) -> AST:
        self.eat('FUNC')
        name = self.eat('IDENT')[1]
        self.eat('PUNCT', '(')
        self.eat('PUNCT', ')')
        
        return_type = None
        if self.current_token and self.current_token[0] == 'TYPE':
            return_type = self.eat('TYPE')[1]
        
        self.eat('PUNCT', '{')
        
        body = []
        while self.current_token and self.current_token[1] != '}':
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
        
        self.eat('PUNCT', '}')
        
        return AST('Function', f"{name}:{return_type}" if return_type else name, body)
    
    def parse_statement(self) -> AST:
        if not self.current_token:
            return None
            
        if self.current_token[0] == 'PRINT':
            return self.parse_print()
        elif self.current_token[0] == 'TYPE':
            return self.parse_var_decl()
        elif self.current_token[0] == 'IDENT':
            next_token = self.tokens[self.pos + 1] if self.pos + 1 < len(self.tokens) else None
            if next_token and next_token[1] == '(':
                return self.parse_function_call()
            elif next_token and next_token[0] == 'ASSIGN':
                return self.parse_assignment()
        elif self.current_token[0] == 'RETURN':
            return self.parse_return()
        
        # Skip unknown
        self.eat()
        return None
    
    def parse_print(self) -> AST:
        self.eat('PRINT')
        self.eat('PUNCT', '(')
        expr = self.parse_expression()
        self.eat('PUNCT', ')')
        return AST('Print', children=[expr])
    
    def parse_return(self) -> AST:
        self.eat('RETURN')
        expr = self.parse_expression() if self.current_token and self.current_token[0] != 'PUNCT' else None
        return AST('Return', children=[expr] if expr else [])
    
    def parse_var_decl(self) -> AST:
        var_type = self.eat('TYPE')[1]
        name = self.eat('IDENT')[1]
        
        init = None
        if self.current_token and self.current_token[0] == 'ASSIGN':
            self.eat('ASSIGN')
            init = self.parse_expression()
        
        return AST('VarDecl', f"{name}:{var_type}", [init] if init else [])
    
    def parse_assignment(self) -> AST:
        name = self.eat('IDENT')[1]
        self.eat('ASSIGN')
        value = self.parse_expression()
        return AST('Assign', name, [value])
    
    def parse_function_call(self) -> AST:
        name = self.eat('IDENT')[1]
        self.eat('PUNCT', '(')
        
        args = []
        while self.current_token and self.current_token[1] != ')':
            args.append(self.parse_expression())
            if self.current_token and self.current_token[1] == ',':
                self.eat('PUNCT', ',')
        
        self.eat('PUNCT', ')')
        return AST('Call', name, args)
    
    def parse_expression(self) -> AST:
        left = self.parse_term()
        
        while self.current_token and self.current_token[0] in ['OP', 'COMPARE']:
            op = self.eat()[1]
            right = self.parse_term()
            left = AST('BinaryOp', op, [left, right])
        
        return left
    
    def parse_term(self) -> AST:
        left = self.parse_factor()
        
        while self.current_token and self.current_token[0] == 'OP' and self.current_token[1] in ['*', '/']:
            op = self.eat()[1]
            right = self.parse_factor()
            left = AST('BinaryOp', op, [left, right])
        
        return left
    
    def parse_factor(self) -> AST:
        if not self.current_token:
            raise SyntaxError("Unexpected end in expression")
        
        token = self.current_token
        
        if token[0] == 'IDENT':
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][1] == '(':
                return self.parse_function_call()
            else:
                return AST('Variable', self.eat('IDENT')[1])
        elif token[0] == 'NUMBER':
            return AST('Number', self.eat('NUMBER')[1])
        elif token[0] == 'STRING':
            value = self.eat('STRING')[1][1:-1]  # Remove quotes
            return AST('String', value)
        elif token[1] == '(':
            self.eat('PUNCT', '(')
            expr = self.parse_expression()
            self.eat('PUNCT', ')')
            return expr
        else:
            raise SyntaxError(f"Unexpected token in expression: {token[1]}")

def parse(tokens: List[tuple]) -> AST:
    return Parser(tokens).parse()