# src/compiler/bytecode.py
from enum import Enum
import struct
from typing import List, Dict, Any

class OpCode(Enum):
    # Stack operations
    LOAD_CONST = 1
    LOAD_VAR = 2
    STORE_VAR = 3
    
    # Arithmetic
    ADD = 10
    SUB = 11
    MUL = 12
    DIV = 13
    
    # Control flow
    CALL = 30
    RETURN = 31
    
    # Built-ins
    PRINT = 40
    
    # Program
    HALT = 255

class BytecodeCompiler:
    def __init__(self):
        self.code: List[tuple] = []  # (opcode, operand)
        self.constants: List[Any] = []
        self.variables: Dict[str, int] = {}  # {name: index}
    
    def compile(self, ast) -> bytes:
        """Compile AST to bytecode"""
        self.code = []
        self.constants = []
        self.variables = {}
        
        print("🔧 Compiling...")
        
        # Find main function
        main_func = None
        for child in ast.children:
            if child.type == 'Function' and child.value == 'main':
                main_func = child
                break
        
        if not main_func:
            raise Exception("No main function found")
        
        print(f"Found main function")
        
        # Compile function body
        for stmt in main_func.children:
            self.compile_node(stmt)
        
        # Add HALT
        self.emit(OpCode.HALT)
        
        print(f"Compiled: {len(self.code)} instructions, {len(self.constants)} constants, {len(self.variables)} variables")
        return self.pack()
    
    def compile_node(self, node):
        node_type = node.type
        
        if node_type == 'Print':
            # print(expr)
            self.compile_node(node.children[0])
            self.emit(OpCode.PRINT)
            
        elif node_type == 'Return':
            # return expr
            if node.children:
                self.compile_node(node.children[0])
            self.emit(OpCode.RETURN)
            
        elif node_type == 'VarDecl':
            # int x = value
            var_name = node.value
            
            # Register variable
            if var_name not in self.variables:
                self.variables[var_name] = len(self.variables)
                print(f"   Registered variable: {var_name} -> {self.variables[var_name]}")
            
            # Compile initialization
            if len(node.children) > 1:  # Has value
                self.compile_node(node.children[1])  # Value is second child
                self.emit(OpCode.STORE_VAR, self.variables[var_name])
                
        elif node_type == 'Assign':
            # x = value
            var_name = node.value
            
            if var_name not in self.variables:
                self.variables[var_name] = len(self.variables)
                print(f"   Registered variable: {var_name} -> {self.variables[var_name]}")
            
            self.compile_node(node.children[0])
            self.emit(OpCode.STORE_VAR, self.variables[var_name])
            
        elif node_type == 'BinaryOp':
            # a + b
            self.compile_node(node.children[0])
            self.compile_node(node.children[1])
            
            op_map = {
                '+': OpCode.ADD,
                '-': OpCode.SUB,
                '*': OpCode.MUL,
                '/': OpCode.DIV
            }
            self.emit(op_map[node.value])
            
        elif node_type == 'Number':
            # 123
            value = float(node.value) if '.' in node.value else int(node.value)
            idx = self.add_constant(value)
            self.emit(OpCode.LOAD_CONST, idx)
            
        elif node_type == 'String':
            # "hello"
            idx = self.add_constant(node.value)
            self.emit(OpCode.LOAD_CONST, idx)
            
        elif node_type == 'Variable':
            # x
            if node.value not in self.variables:
                raise Exception(f"Unknown variable: {node.value}")
            self.emit(OpCode.LOAD_VAR, self.variables[node.value])
    
    def emit(self, opcode: OpCode, operand: int = 0):
        """Add instruction"""
        self.code.append((opcode.value, operand))
    
    def add_constant(self, value: Any) -> int:
        """Add constant to pool"""
        self.constants.append(value)
        return len(self.constants) - 1
    
    def pack(self) -> bytes:
        """Pack to bytecode format"""
        # Header
        header = struct.pack('4sB', b'PYBC', 1)
        
        # Constants
        constants_data = self.pack_constants()
        
        # Code
        code_data = self.pack_code()
        
        return header + constants_data + code_data
    
    def pack_constants(self) -> bytes:
        """Pack constant pool"""
        result = bytearray()
        result.extend(struct.pack('H', len(self.constants)))  # count
        
        for const in self.constants:
            if isinstance(const, int):
                result.append(1)  # type int
                result.extend(struct.pack('i', const))
            elif isinstance(const, float):
                result.append(2)  # type float
                result.extend(struct.pack('d', const))
            elif isinstance(const, str):
                result.append(3)  # type string
                encoded = const.encode('utf-8')
                result.extend(struct.pack('H', len(encoded)))
                result.extend(encoded)
            else:
                # Default to int 0
                result.append(1)
                result.extend(struct.pack('i', 0))
        
        return bytes(result)
    
    def pack_code(self) -> bytes:
        """Pack code instructions"""
        result = bytearray()
        result.extend(struct.pack('I', len(self.code)))  # count
        
        for opcode, operand in self.code:
            result.append(opcode)
            result.extend(struct.pack('i', operand))
        
        return bytes(result)