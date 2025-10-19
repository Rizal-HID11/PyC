from lexer import Token

class ASTNode:
    def __init__(self, ntype, value=None, line=None):
        self.ntype = ntype          # Node type (e.g., print, expr)
        self.value = value          # Optional value of the node
        self.line = line            # Line number in source code
        self.children = []          # Child nodes for tree structure

def parse(tokens):
    ast = []                       # List to store AST nodes
    for t in tokens:
        if t.ttype == "print":     # Handle print statements
            ast.append({"type": "print", "value": t.value})
    return ast                     # Return the constructed AST
