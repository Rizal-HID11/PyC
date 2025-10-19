# src/parser.py
from lexer import Token
from typing import List, Optional

class AST:
    def __init__(self, type: str, value: str = "", children: List['AST'] = None):
        self.type = type
        self.value = value
        self.children = children or []

def parse(tokens: List[Token]) -> AST:
    parser = Parser(tokens)
    return parser.parse()

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
    
    def current(self) -> Optional[Token]:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None
    
    def eat(self, token_type: str = None, value: str = None) -> Token:
        token = self.current()
        if not token:
            raise SyntaxError("Unexpected EOF")
        if token_type and token.type != token_type:
            raise SyntaxError(f"Expected {token_type}, got {token.type}")
        if value and token.value != value:
            raise SyntaxError(f"Expected '{value}', got '{token.value}'")
        self.pos += 1
        return token
    
    def match(self, token_type: str = None, value: str = None) -> bool:
        token = self.current()
        if not token:
            return False
        if token_type and token.type != token_type:
            return False
        if value and token.value != value:
            return False
        return True
    
    def parse(self) -> AST:
        functions = []
        while self.match('KEYWORD', 'func'):
            functions.append(self.parse_function())
        return AST('Program', children=functions)
    
    def parse_function(self) -> AST:
        self.eat('KEYWORD', 'func')
        name = self.eat('IDENT').value
        
        self.eat('PUNCT', '(')
        self.eat('PUNCT', ')')
        
        # Return type
        return_type = 'void'
        if self.match('TYPE'):
            return_type = self.eat('TYPE').value
        
        self.eat('PUNCT', '{')
        
        body = []
        while not self.match('PUNCT', '}'):
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
        
        self.eat('PUNCT', '}')
        
        # Simple: just store name, return type in metadata
        func = AST('Function', name, body)
        func.return_type = return_type  # Store as attribute
        return func
    
    def parse_statement(self) -> AST:
        if self.match('KEYWORD', 'print'):
            return self.parse_print()
        elif self.match('KEYWORD', 'return'):
            return self.parse_return()
        elif self.match('TYPE'):
            return self.parse_var_decl()
        elif self.match('IDENT'):
            return self.parse_assign()
        else:
            raise SyntaxError(f"Unexpected: {self.current().value}")
    
    def parse_print(self) -> AST:
        self.eat('KEYWORD', 'print')
        self.eat('PUNCT', '(')
        expr = self.parse_expr()
        self.eat('PUNCT', ')')
        return AST('Print', children=[expr])
    
    def parse_return(self) -> AST:
        self.eat('KEYWORD', 'return')
        expr = self.parse_expr() if not self.match('PUNCT', ';') else None
        return AST('Return', children=[expr] if expr else [])
    
    def parse_var_decl(self) -> AST:
        type_tok = self.eat('TYPE')
        name = self.eat('IDENT').value
        
        value = None
        if self.match('OP', '='):
            self.eat('OP', '=')
            value = self.parse_expr()
        
        return AST('VarDecl', name, [AST('Type', type_tok.value), value] if value else [AST('Type', type_tok.value)])
    
    def parse_assign(self) -> AST:
        name = self.eat('IDENT').value
        self.eat('OP', '=')
        value = self.parse_expr()
        return AST('Assign', name, [value])
    
    def parse_expr(self) -> AST:
        left = self.parse_term()
        
        while self.match('OP') and self.current().value in ['+', '-', '*', '/']:
            op = self.eat('OP').value
            right = self.parse_term()
            left = AST('BinaryOp', op, [left, right])
        
        return left
    
    def parse_term(self) -> AST:
        if self.match('NUMBER'):
            return AST('Number', self.eat('NUMBER').value)
        elif self.match('STRING'):
            text = self.eat('STRING').value
            return AST('String', text[1:-1])  # Remove quotes
        elif self.match('IDENT'):
            return AST('Variable', self.eat('IDENT').value)
        elif self.match('PUNCT', '('):
            self.eat('PUNCT', '(')
            expr = self.parse_expr()
            self.eat('PUNCT', ')')
            return expr
        else:
            raise SyntaxError(f"Unexpected term: {self.current().value}")