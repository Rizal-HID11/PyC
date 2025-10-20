# src/main.py
from lexer import tokenize
from parser import parse
from compiler.bytecode import Compiler
from vm.machine import VM

def compile_and_run(source_file: str):
    print(f"PyC - {source_file}")
    
    with open(source_file, 'r') as f:
        source = f.read()
    
    print("Source:")
    print(source)
    print()
    
    # Lex
    tokens = list(tokenize(source))
    print(f"Tokens: {len(tokens)}")
    
    # Parse
    try:
        ast = parse(tokens)
        print(f"AST: {ast.type} with {len(ast.children)} children")
        
        # DEBUG: Print AST structure
        if ast.children:
            print("AST Structure:")
            for i, child in enumerate(ast.children):
                print(f"   {i}: {child.type} '{child.value}' with {len(child.children)} children")
        else:
            print("WARNING: AST has no children!")
            
    except Exception as e:
        print(f"Parser Error: {e}")
        return
    
    # Compile
    compiler = Compiler()
    bytecode = compiler.compile(ast)
    
    # Execute
    print("Execution:")
    print("-" * 30)
    vm = VM()
    vm.load(bytecode)
    vm.run()
    print("-" * 30)

if __name__ == "__main__":
    compile_and_run("examples/hello.pyc")