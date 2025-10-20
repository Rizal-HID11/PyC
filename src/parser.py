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
                elif self.current_token[0] == 'IF':
                    stmt = self.parse_if()
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
    
    def parse_if(self) -> AST:
        """Parse if/else statement"""
        self.eat('IF') # Consume 'if'
        self.eat("PUNCT", "(")

        # Parse condition
        condition = self.parse_expression()

        self.eat('PUNCT', ')')
        self.eat('PUNCT', '{')

        # Parse then branch (statements inside {})
        then_statements = []
        while self.current_token and self.current_token[1] != '}':
            stmt = self.parse_statement()
            if stmt:
                then_statements.append(stmt)
        self.eat('PUNCT', '}')
        print(f"🐛 DEBUG parse_if: then_statements = {len(then_statements)} statements")

        #Parse else branch
        else_statements = []
        if self.current_token and self.current_token[0] == 'ELSE':
            self.eat('ELSE')
            self.eat('PUNCT', '{')

            while self.current_token and self.current_token[1] != '}':
                stmt = self.parse_statement()
                if stmt:
                    else_statements.append(stmt)
            self.eat('PUNCT', '}')
        
        #Create AST nodes for blocks
        then_block = AST('Block', children=then_statements)
        else_block = AST('Block', children=else_statements)

        result =  AST('If', children=[condition, then_block, else_block])
        return result
    
    def parse_statement(self) -> AST:
        if not self.current_token:
            return None
                
        # PRINT STATEMENT
        if self.current_token[0] == 'PRINT':
            return self.parse_print()
        
        # VAR DECLARATION
        elif self.current_token[0] == 'TYPE':
            return self.parse_var_decl()
        
        # IF STATEMENT
        elif self.current_token[0] == 'IF':
            return self.parse_if()

        # RETURN STATEMENT
        elif self.current_token[0] == 'RETURN':
            return self.parse_return()
        
        # IDENTIFIER-BASED STATEMENTS
        elif self.current_token[0] == 'IDENT':
            next_token = self.tokens[self.pos + 1] if self.pos + 1 < len(self.tokens) else None
            print(f"DEBUG parse_statement: IDENT with next_token = {next_token}")

            # FUNC CALL: ident(
            if next_token and next_token[1] == '(':
                return self.parse_function_call()

            # ASSIGNMENT ident = value
            elif next_token and next_token[0] == 'ASSIGN':
                return self.parse_assignment()
            
            # ARRAY OP: ident[ index ]
            elif next_token and next_token[1] == '[':
                print("DEBUG: Found array operation!")
                array_access = self.parse_array_access()

                # Check if it's assignment
                if self.current_token and self.current_token[0] == 'ASSIGN':
                    self.eat('ASSIGN')
                    value = self.parse_expression()
                    return AST('ArrayAssign', children=[array_access, value])
                else:
                    return array_access # Just array access in statement context
        
        #Skip unknown
        self.eat()
        return None
    
    def parse_print(self) -> AST:
        self.eat('PRINT')
        self.eat('PUNCT', '(')
        
        # Parse multiple arguments
        args = []
        while self.current_token and self.current_token[1] != ')':
            args.append(self.parse_expression())
            if self.current_token and self.current_token[1] == ',':
                self.eat('PUNCT', ',')
            else:
                break
        
        self.eat('PUNCT', ')')
        return AST('Print', children=args) 
    
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

    def parse_array_literal(self) -> AST:
        # Handle [1, 2, 3]
        self.eat('LBRACKET')
        elements = []
        while self.current_token and self.current_token[1] != ']':
            elements.append(self.parse_expression())
            if self.current_token and self.current_token[1] == ',':
                self.eat('PUNCT', ',')
        self.eat('RBRACKET')
        return AST('ArrayLiteral', children=elements)

    def parse_array_access(self) -> AST: 
        # Handle arr[index]
        array_name = self.eat('IDENT')[1]
        self.eat('LBRACKET')
        index_expr = self.parse_expression()
        self.eat('RBRACKET')
        return AST('ArrayAccess', value=array_name, children=[index_expr])
    
    def parse_expression(self) -> AST:
        
        # Handle array literals first
        if self.current_token and self.current_token[1] == '[':
            return self.parse_array_literal()
        
        # Then handle normal expressions
        left = self.parse_term()

        while self.current_token and self.current_token[0] in ['OP', 'COMPARE']:
            op = self.eat()[1]
            right = self.parse_term()
            left = AST('BinaryOp', op, [left, right])

        return left
    
    def parse_term(self) -> AST:

        # Handle array literals in terms too
        if self.current_token and self.current_token[1] == '[':
            return self.parse_array_literal()
        
        left = self.parse_factor()

        while self.current_token and self.current_token[0] == 'OP' and self.current_token[1] in ['*', '/']:
            op = self.eat()[1]
            right = self.parse_factor()
            left = AST('BinaryOp', op, [left, right])

        return left
    
    def parse_factor(self) -> AST:
        print(f"DEBUG parse_factor: current_token = {self.current_token}")

        if not self.current_token:
            raise SyntaxError("Unexpected end in expression")
        
        token = self.current_token

        
        if token[0] == 'IDENT':
            next_token = self.tokens[self.pos + 1] if self.pos + 1 < len(self.tokens) else None

            if next_token and next_token[1] == '[':
                return self.parse_array_access()
            elif next_token and next_token[1] == '(':
                return self.parse_function_call()
            else:
                return AST('Variable', self.eat('IDENT')[1])

        elif token[1] == '[':
            return self.parse_array_literal()
        
        elif token[0] == 'NUMBER':
            return AST('Number', self.eat('NUMBER')[1])

        elif token[0] == 'STRING':
            value = self.eat('STRING')[1][1:-1]
            return AST('String', value)

        elif token[1] == '(':
            self.eat('PUNCT', '(')
            expr = self.parse_expression()
            self.eat('PUNCT', ')')
            return expr
            
        else:
            raise SyntaxError(f"Unextpected token in expression: {token[1]}")


def parse(tokens: List[tuple]) -> AST:
    return Parser(tokens).parse()