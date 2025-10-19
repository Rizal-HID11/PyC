from lexer import Token

class ASTNode:
    def __init__(self, ntype, value=None, line=None):
        self.ntype = ntype
        self.value = value
        self.line = line
        self.children = []

def parse(tokens):
    ast = []
    for t in tokens:
        if t.ttype == "print":
            ast.append({"type": "print", "value": t.value})
    return ast

