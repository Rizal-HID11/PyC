# src/compiler/bytecode.py
from enum import Enum
import struct
from typing import Any, Dict, List

class OpCode(Enum):
    # Stack operations
    LOAD_CONST = 1
    LOAD_VAR = 2
    STORE_VAR = 3
    POP = 4
    
    # Arithmetic operations
    ADD = 10
    SUB = 11
    MUL = 12
    DIV = 13
    
    # Comparison operations
    EQ = 20
    NEQ = 21
    GT = 22
    LT = 23
    GTE = 24
    LTE = 25
    
    # Control flow
    JUMP = 30
    JUMP_IF_FALSE = 31
    JUMP_IF_TRUE = 32
    CALL = 33
    RETURN = 34
    
    # Built-ins
    PRINT = 40
    
    # Program control
    HALT = 255

class Compiler:
    def __init__(self):
        self.code = []
        self.constants = []
        self.variables = {}
        self.functions = {}
        self.labels = {}  # For jump targets
        self.label_counter = 0
    
    def compile(self, ast) -> bytes:
        print("🔧 Compilation Started")
        
        # Find all functions first
        for stmt in ast.children:
            if stmt.type == 'Function':
                func_name = stmt.value.split(':')[0] if ':' in stmt.value else stmt.value
                self.functions[func_name] = len(self.code)
                print(f"📍 Function '{func_name}' at position {len(self.code)}")
        
        # Compile all statements
        for stmt in ast.children:
            self.compile_statement(stmt)
        
        # Resolve all labels
        self.resolve_labels()
        
        # Add halt if needed
        if not self.code or self.code[-1][0] != OpCode.HALT.value:
            self.emit(OpCode.HALT)
        
        print(f"✅ Compilation Complete: {len(self.code)} instructions")
        return self.serialize()
    
    def compile_statement(self, stmt):
        if stmt.type == 'Function':
            self.compile_function(stmt)
        elif stmt.type == 'Print':
            self.compile_print(stmt)
        elif stmt.type == 'VarDecl':
            self.compile_var_decl(stmt)
        elif stmt.type == 'Assign':
            self.compile_assign(stmt)
        elif stmt.type == 'Call':
            self.compile_call(stmt)
        elif stmt.type == 'If':
            self.compile_if(stmt)
        elif stmt.type == 'ExprStmt':
            expr = stmt.children[0]
            if expr.type == 'Call':
                self.compile_call(expr)
            else:
                self.compile_expression(expr)
                self.emit(OpCode.POP)
    
    def compile_function(self, func):
        func_name = func.value.split(':')[0] if ':' in func.value else func.value
        print(f"🔨 Compiling function: {func_name}")
        
        # Save current state
        old_vars = self.variables.copy()
        self.variables = {}  # New scope
        
        # Update function position
        self.functions[func_name] = len(self.code)
        
        # Compile function body
        for stmt in func.children:
            self.compile_statement(stmt)
        
        # Add return if missing
        if not any(child.type == 'Return' for child in func.children):
            self.emit(OpCode.LOAD_CONST, self.add_constant(0))
            self.emit(OpCode.RETURN)
        
        # Restore state
        self.variables = old_vars
    
    def compile_print(self, stmt):
        self.compile_expression(stmt.children[0])
        self.emit(OpCode.PRINT)
    
    def compile_var_decl(self, stmt):
        var_name = stmt.value.split(':')[0]
        if var_name not in self.variables:
            self.variables[var_name] = len(self.variables)
        
        if stmt.children:  # Has initial value
            self.compile_expression(stmt.children[0])
            self.emit(OpCode.STORE_VAR, self.variables[var_name])
    
    def compile_assign(self, stmt):
        var_name = stmt.value
        if var_name not in self.variables:
            self.variables[var_name] = len(self.variables)
        
        self.compile_expression(stmt.children[0])
        self.emit(OpCode.STORE_VAR, self.variables[var_name])
    
    def compile_call(self, call):
        func_name = call.value
        
        if func_name not in self.functions:
            raise Exception(f"Undefined function: {func_name}")
        
        # Compile arguments
        for arg in call.children:
            self.compile_expression(arg)
        
        self.emit(OpCode.CALL, self.functions[func_name])
        self.emit(OpCode.POP)  # Discard return value
    
    def compile_if(self, stmt):
        # condition, then_block, else_block
        self.compile_expression(stmt.children[0])  # Condition
        
        else_label = self.new_label()
        end_label = self.new_label()
        
        # Jump to else if condition is false
        self.emit(OpCode.JUMP_IF_FALSE, else_label)
        
        # Compile then block
        for then_stmt in stmt.children[1].children:
            self.compile_statement(then_stmt)
        
        # Jump to end after then block
        self.emit(OpCode.JUMP, end_label)
        
        # Else block
        self.place_label(else_label)
        for else_stmt in stmt.children[2].children:
            self.compile_statement(else_stmt)
        
        self.place_label(end_label)
    
    def compile_expression(self, expr):
        if expr.type == 'String':
            const_idx = self.add_constant(expr.value)
            self.emit(OpCode.LOAD_CONST, const_idx)
        elif expr.type == 'Number':
            value = float(expr.value) if '.' in expr.value else int(expr.value)
            const_idx = self.add_constant(value)
            self.emit(OpCode.LOAD_CONST, const_idx)
        elif expr.type == 'Variable':
            if expr.value not in self.variables:
                raise Exception(f"Undefined variable: {expr.value}")
            self.emit(OpCode.LOAD_VAR, self.variables[expr.value])
        elif expr.type == 'BinaryOp':
            self.compile_binary_op(expr)
        elif expr.type == 'Call':
            self.compile_call(expr)
    
    def compile_binary_op(self, expr):
        # Compile left and right operands
        self.compile_expression(expr.children[0])
        self.compile_expression(expr.children[1])
        
        # Emit the operation
        op_map = {
            '+': OpCode.ADD,
            '-': OpCode.SUB,
            '*': OpCode.MUL,
            '/': OpCode.DIV,
            '==': OpCode.EQ,
            '!=': OpCode.NEQ,
            '>': OpCode.GT,
            '<': OpCode.LT,
            '>=': OpCode.GTE,
            '<=': OpCode.LTE
        }
        
        if expr.value in op_map:
            self.emit(op_map[expr.value])
        else:
            raise Exception(f"Unsupported operator: {expr.value}")
    
    def new_label(self):
        self.label_counter += 1
        return self.label_counter
    
    def place_label(self, label):
        self.labels[label] = len(self.code)
    
    def resolve_labels(self):
        """Replace label IDs with actual code positions"""
        resolved_code = []
        for opcode, operand in self.code:
            if opcode in [OpCode.JUMP.value, OpCode.JUMP_IF_FALSE.value, OpCode.JUMP_IF_TRUE.value]:
                # Replace label ID with actual position
                if operand in self.labels:
                    resolved_code.append((opcode, self.labels[operand]))
                else:
                    resolved_code.append((opcode, operand))
            else:
                resolved_code.append((opcode, operand))
        self.code = resolved_code
    
    def emit(self, opcode: OpCode, operand: int = 0):
        self.code.append((opcode.value, operand))
        print(f"   💾 {opcode.name} {operand}")
    
    def add_constant(self, value: Any) -> int:
        self.constants.append(value)
        return len(self.constants) - 1
    
    def serialize(self) -> bytes:
        result = bytearray(b'PYBC\x01')
        
        # Constants
        result.extend(struct.pack('H', len(self.constants)))
        for const in self.constants:
            if isinstance(const, str):
                result.append(1)
                encoded = const.encode('utf-8')
                result.extend(struct.pack('H', len(encoded)))
                result.extend(encoded)
            elif isinstance(const, int):
                result.append(2)
                result.extend(struct.pack('i', const))
            elif isinstance(const, float):
                result.append(3)
                result.extend(struct.pack('d', const))
        
        # Code
        result.extend(struct.pack('I', len(self.code)))
        for op, operand in self.code:
            result.append(op)
            result.extend(struct.pack('i', operand))
        
        return bytes(result)