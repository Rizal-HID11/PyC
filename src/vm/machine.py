# src/vm/machine.py
import struct
from compiler.bytecode import OpCode

class VM:
    def __init__(self):
        self.stack = []
        self.vars = [None] * 100
        self.constants = []
        self.code = []
        self.pc = 0
        self.call_stack = []
    
    def load(self, bytecode: bytes):
        if bytecode[:4] != b'PYBC':
            raise Exception("Invalid bytecode")
        
        pos = 5
        
        # Constants
        const_count = struct.unpack('H', bytecode[pos:pos+2])[0]
        pos += 2
        
        self.constants = []
        for _ in range(const_count):
            const_type = bytecode[pos]
            pos += 1
            
            if const_type == 1:  # String
                length = struct.unpack('H', bytecode[pos:pos+2])[0]
                pos += 2
                value = bytecode[pos:pos+length].decode('utf-8')
                pos += length
                self.constants.append(value)
            elif const_type == 2:  # Integer
                value = struct.unpack('i', bytecode[pos:pos+4])[0]
                pos += 4
                self.constants.append(value)
            elif const_type == 3:  # Float
                value = struct.unpack('d', bytecode[pos:pos+8])[0]
                pos += 8
                self.constants.append(value)
        
        # Code
        code_count = struct.unpack('I', bytecode[pos:pos+4])[0]
        pos += 4
        
        self.code = []
        for _ in range(code_count):
            opcode = bytecode[pos]
            operand = struct.unpack('i', bytecode[pos+1:pos+5])[0]
            pos += 5
            self.code.append((opcode, operand))
        
        print(f"VM loaded: {len(self.constants)} constants, {len(self.code)} instructions")
    
    def run(self):
        self.pc = 0
        self.stack = []
        self.call_stack = []
        
        print("VM Execution Started")
        
        try:
            while self.pc < len(self.code):
                op, arg = self.code[self.pc]
                self.execute(OpCode(op), arg)
                self.pc += 1
        except Exception as e:
            print(f"VM Error at instruction {self.pc}: {e}")
            raise
        
        print("VM Execution Finished")
    
    def execute(self, opcode: OpCode, arg: int):
        try:
            if opcode == OpCode.LOAD_CONST:
                self.stack.append(self.constants[arg])
            
            elif opcode == OpCode.LOAD_VAR:
                self.stack.append(self.vars[arg])
            
            elif opcode == OpCode.STORE_VAR:
                self.vars[arg] = self.stack.pop()
            
            elif opcode == OpCode.POP:
                self.stack.pop()
            
            # Arithmetic operations
            elif opcode == OpCode.ADD:
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a + b)
            
            elif opcode == OpCode.SUB:
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a - b)
            
            elif opcode == OpCode.MUL:
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a * b)
            
            elif opcode == OpCode.DIV:
                b, a = self.stack.pop(), self.stack.pop()
                if b == 0:
                    raise Exception("Division by zero!")
                self.stack.append(a / b)
            
            # Comparison operations - FIXED ORDER
            elif opcode == OpCode.GT:
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a > b)
            
            elif opcode == OpCode.LT:
                a, b = self.stack.pop(), self.stack.pop()
                self.stack.append(a < b)
            
            elif opcode == OpCode.EQ:
                a, b = self.stack.pop(), self.stack.pop()
                self.stack.append(a == b)

            elif opcode == OpCode.NEQ:
                a, b = self.stack.pop(), self.stack.pop()
                self.stack.append(a != b)
            
            elif opcode == OpCode.GTE:
                a, b = self.stack.pop(), self.stack.pop()
                self.stack.append(a >= b)
            
            elif opcode == OpCode.LTE:
                print(f"DEBUG {opcode.name} arg={arg}, stack={self.stack}")
                a, b = self.stack.pop(), self.stack.pop()
                self.stack.append(a <= b)
            
            
            # Control flow
            elif opcode == OpCode.JUMP:
                self.pc = arg - 1  # -1 because we increment after
            
            elif opcode == OpCode.JUMP_IF_FALSE:
                condition_value = self.stack.pop()
                if not condition_value:
                    self.pc = arg - 1
                else:
                    print(f"DEBUG: NOT jumping, condition is True")
            
            elif opcode == OpCode.JUMP_IF_TRUE:
                if self.stack.pop():
                    self.pc = arg - 1
            
            elif opcode == OpCode.CALL:
                self.call_stack.append(self.pc)
                self.pc = arg - 1
            
            elif opcode == OpCode.RETURN:
                if self.call_stack:
                    self.pc = self.call_stack.pop()
                else:
                    self.pc = len(self.code)
            
            # Arrays
            elif opcode == OpCode.CREATE_ARRAY:
                size = arg
                array = []
                for _ in range(size):
                    array.append(self.stack.pop())
                array.reverse()
                self.stack.append(array)

            elif opcode == OpCode.LOAD_ARRAY:
                index = self.stack.pop()
                array = self.stack.pop()
                self.stack.append(array[index])

            elif opcode == OpCode.STORE_ARRAY:
                value = self.stack.pop()
                index = self.stack.pop()
                array = self.stack.pop()
                array[index] = value
                self.stack.append(value)
            
            # Built-ins
            elif opcode == OpCode.PRINT:
                value = self.stack.pop()
                if isinstance(value, bool):
                    print("true" if value else "false", end=" ") # Print boolean as string
                else:
                    print(value, end=" ")
            
            elif opcode == OpCode.PRINT_END:
                print() # Newline after complete all arguments
            
            elif opcode == OpCode.HALT:
                self.pc = len(self.code)
            
            else:
                raise Exception(f"Unknown opcode: {opcode}")
                
        except Exception as e:
            raise Exception(f"Error executing {opcode}: {e}")