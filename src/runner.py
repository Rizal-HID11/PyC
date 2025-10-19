from parser import ASTNode

def run(ast):
    for node in ast:
        if node["type"] == "print":
            print(node["value"].strip('"'))


