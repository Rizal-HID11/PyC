# src/main.py
from lexer import tokenize
from parser import parse
from compiler.bytecode import BytecodeCompiler, OpCode
from vm.machine import VirtualMachine

def compile_and_run(source_file: str):
    print(f"PyC Compiler - {source_file}")
    
    with open(source_file, 'r') as f:
        source = f.read()
    
    print("Source:")
    print(source)
    print()
    
    try:
        # Lex
        tokens = tokenize(source)
        print(f"Tokens: {len(tokens)}")
        for t in tokens[:10]:  # Show first 10 tokens
            print(f"   {t.type:8} '{t.value}'")
        print()
        
        # Parse
        ast = parse(tokens)
        print(f"AST: {ast.type} with {len(ast.children)} children")
        for i, child in enumerate(ast.children):
            print(f"   Child {i}: {child.type} '{child.value}' with {len(child.children)} children")
        
        # Compile to bytecode
        compiler = BytecodeCompiler()
        bytecode = compiler.compile(ast)
        
        print(f"Bytecode compiled:")
        print(f"   Constants: {compiler.constants}")
        print(f"   Variables: {compiler.variables}")
        print(f"   Code: {len(compiler.code)} instructions")
        
        # Fix: Use OpCode directly, not BytecodeCompiler.OpCode
        for i, (op, operand) in enumerate(compiler.code):
            op_name = [opcode.name for opcode in OpCode if opcode.value == op][0]
            print(f"      {i:2d}: {op_name:10} {operand}")
        print()
        
        # Save
        bytecode_file = source_file.replace('.pyc', '.pbc')
        with open(bytecode_file, 'wb') as f:
            f.write(bytecode)
        
        print(f"Saved: {bytecode_file}")
        print()
        
        # Run in VM
        print("VM Execution:")
        print("=" * 30)
        vm = VirtualMachine()
        vm.load(bytecode)
        vm.run()
        print("=" * 30)
        print("Execution completed!")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    compile_and_run("examples/hello.pyc")