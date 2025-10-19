# src/vm/machine.py
import struct
from typing import List, Any
from compiler.bytecode import OpCode

class VirtualMachine:
    def __init__(self):
        self.stack: List[Any] = []
        self.variables: List[Any] = []
        self.constants: List[Any] = []
        self.code: List[tuple] = []  # (opcode, operand)
        self.pc: int = 0  # Program counter
    
    def load(self, bytecode: bytes):
        """Load bytecode into VM"""
        self.stack = []
        self.variables = [None] * 100  # Pre-allocate variable space
        self.constants = []
        self.code = []
        self.pc = 0
        
        # Parse header
        if len(bytecode) < 5:
            raise Exception("Invalid bytecode: too short")
        
        magic, version = struct.unpack('4sB', bytecode[:5])
        if magic != b'PYBC':
            raise Exception("Invalid bytecode format")
        
        offset = 5
        
        # Parse constants section
        const_count = struct.unpack('H', bytecode[offset:offset+2])[0]
        offset += 2
        
        for i in range(const_count):
            if offset >= len(bytecode):
                raise Exception("Invalid bytecode: truncated constants")
            
            const_type = bytecode[offset]
            offset += 1
            
            if const_type == 1:  # Integer
                if offset + 4 > len(bytecode):
                    raise Exception("Invalid bytecode: truncated integer")
                value = struct.unpack('i', bytecode[offset:offset+4])[0]
                offset += 4
                self.constants.append(value)
                
            elif const_type == 2:  # Float
                if offset + 8 > len(bytecode):
                    raise Exception("Invalid bytecode: truncated float")
                value = struct.unpack('d', bytecode[offset:offset+8])[0]
                offset += 8
                self.constants.append(value)
                
            elif const_type == 3:  # String
                if offset + 2 > len(bytecode):
                    raise Exception("Invalid bytecode: truncated string length")
                str_len = struct.unpack('H', bytecode[offset:offset+2])[0]
                offset += 2
                if offset + str_len > len(bytecode):
                    raise Exception("Invalid bytecode: truncated string data")
                value = bytecode[offset:offset+str_len].decode('utf-8')
                offset += str_len
                self.constants.append(value)
                
            else:
                raise Exception(f"Unknown constant type: {const_type}")
        
        # Parse code section
        if offset + 4 > len(bytecode):
            raise Exception("Invalid bytecode: missing code count")
        
        code_count = struct.unpack('I', bytecode[offset:offset+4])[0]
        offset += 4
        
        for i in range(code_count):
            if offset + 5 > len(bytecode):
                raise Exception(f"Invalid bytecode: truncated code at instruction {i}")
            
            opcode = bytecode[offset]
            operand = struct.unpack('i', bytecode[offset+1:offset+5])[0]
            offset += 5
            self.code.append((opcode, operand))
        
        print(f"DEBUG: Loaded {len(self.constants)} constants, {len(self.code)} instructions")
    
    def run(self):
        """Execute the loaded bytecode"""
        self.pc = 0
        
        while self.pc < len(self.code):
            opcode, operand = self.code[self.pc]
            self._execute_instruction(OpCode(opcode), operand)
            self.pc += 1
    
    def _execute_instruction(self, opcode: OpCode, operand: int):
        """Execute a single instruction"""
        try:
            if opcode == OpCode.LOAD_CONST:
                # Push constant to stack
                if operand < len(self.constants):
                    self.stack.append(self.constants[operand])
                else:
                    raise Exception(f"Invalid constant index: {operand}")
                    
            elif opcode == OpCode.LOAD_VAR:
                # Push variable to stack
                if operand < len(self.variables):
                    self.stack.append(self.variables[operand])
                else:
                    raise Exception(f"Invalid variable index: {operand}")
                    
            elif opcode == OpCode.STORE_VAR:
                # Pop stack to variable
                if operand < len(self.variables):
                    if self.stack:
                        self.variables[operand] = self.stack.pop()
                    else:
                        raise Exception("Stack underflow")
                else:
                    raise Exception(f"Invalid variable index: {operand}")
                    
            elif opcode == OpCode.ADD:
                # Addition
                if len(self.stack) >= 2:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a + b)
                else:
                    raise Exception("Stack underflow for ADD")
                    
            elif opcode == OpCode.SUB:
                # Subtraction
                if len(self.stack) >= 2:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a - b)
                else:
                    raise Exception("Stack underflow for SUB")
                    
            elif opcode == OpCode.MUL:
                # Multiplication
                if len(self.stack) >= 2:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a * b)
                else:
                    raise Exception("Stack underflow for MUL")
                    
            elif opcode == OpCode.DIV:
                # Division
                if len(self.stack) >= 2:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    if b == 0:
                        raise Exception("Division by zero")
                    self.stack.append(a / b)
                else:
                    raise Exception("Stack underflow for DIV")
                    
            elif opcode == OpCode.PRINT:
                # Print top of stack
                if self.stack:
                    value = self.stack.pop()
                    print(value)
                else:
                    raise Exception("Stack underflow for PRINT")
                    
            elif opcode == OpCode.RETURN:
                # Return from function (pop return value)
                if self.stack:
                    self.stack.pop()
                    
            elif opcode == OpCode.HALT:
                # Stop execution
                self.pc = len(self.code)
                
            else:
                raise Exception(f"Unknown opcode: {opcode}")
                
        except Exception as e:
            print(f"VM Error at instruction {self.pc} ({opcode}): {e}")
            raise