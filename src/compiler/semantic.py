# src/compiler/semantic.py
class SemanticAnalyzer:
    def __init__(self):
        self.symbols = {}  # {name: {'type': type, 'kind': 'variable|function'}}
        self.errors = []
        self.current_function = None
    
    def analyze(self, ast):
        self.symbols = {}
        self.errors = []
        self.current_function = None
        
        # Add built-in functions
        self.symbols['print'] = {'type': 'void', 'kind': 'function'}
        
        self._analyze_node(ast)
        return len(self.errors) == 0, self.errors
    
    def _analyze_node(self, node):
        method_name = f'_analyze_{node.node_type}'
        method = getattr(self, method_name, lambda n: None)
        method(node)
    
    def _analyze_program(self, node):
        for child in node.children:
            self._analyze_node(child)
    
    def _analyze_function(self, node):
        func_name = node.value
        
        if func_name in self.symbols:
            self._error(f"Function '{func_name}' already defined", node)
            return
        
        # Register function
        self.symbols[func_name] = {
            'type': node.data_type or 'void',
            'kind': 'function',
            'node': node
        }
        
        old_function = self.current_function
        old_symbols = self.symbols.copy()
        
        self.current_function = func_name
        
        # Analyze parameters
        for child in node.children:
            if child.node_type == 'parameter':
                param_name = child.value
                if param_name in self.symbols:
                    self._error(f"Parameter '{param_name}' already defined", child)
                else:
                    self.symbols[param_name] = {
                        'type': child.data_type,
                        'kind': 'variable'
                    }
        
        # Analyze function body
        for child in node.children:
            if child.node_type != 'parameter':
                self._analyze_node(child)
        
        self.current_function = old_function
        self.symbols = old_symbols
    
    def _analyze_variable_declaration(self, node):
        var_name = node.value
        
        if var_name in self.symbols:
            self._error(f"Variable '{var_name}' already declared", node)
            return
        
        self.symbols[var_name] = {
            'type': node.data_type,
            'kind': 'variable'
        }
        
        # Check initialization
        if node.children:
            self._check_assignment(node.data_type, node.children[0], node)
    
    def _analyze_assignment(self, node):
        var_name = node.value
        
        if var_name not in self.symbols:
            self._error(f"Undefined variable '{var_name}'", node)
            return
        
        var_info = self.symbols[var_name]
        
        if node.children:
            self._check_assignment(var_info['type'], node.children[0], node)
    
    def _analyze_function_call(self, node):
        func_name = node.value
        
        if func_name not in self.symbols:
            self._error(f"Undefined function '{func_name}'", node)
            return
        
        # TODO: Check argument types and count
        # For now, just verify function exists
    
    def _analyze_print_statement(self, node):
        if node.children:
            self._analyze_node(node.children[0])
    
    def _analyze_return_statement(self, node):
        if not self.current_function:
            self._error("Return statement outside function", node)
            return
        
        func_info = self.symbols[self.current_function]
        return_type = func_info['type']
        
        if node.children and return_type == 'void':
            self._error(f"Function '{self.current_function}' returns void but has return value", node)
        elif not node.children and return_type != 'void':
            self._error(f"Function '{self.current_function}' must return a value", node)
        elif node.children and return_type != 'void':
            # Check return type compatibility
            expr_type = self._get_expression_type(node.children[0])
            if expr_type != return_type and not (return_type == 'float' and expr_type == 'int'):
                self._error(f"Return type mismatch: expected {return_type}, got {expr_type}", node)
    
    def _check_assignment(self, target_type, value_node, context_node):
        """Check if assignment type is compatible"""
        value_type = self._get_expression_type(value_node)
        
        # Allow int to float conversion
        if target_type == 'float' and value_type == 'int':
            return True
        
        if target_type != value_type:
            self._error(f"Type mismatch: cannot assign {value_type} to {target_type}", context_node)
            return False
        
        return True
    
    def _get_expression_type(self, node):
        """Infer expression type"""
        if node.node_type == 'literal':
            if node.value in ['true', 'false']:
                return 'bool'
            elif '.' in node.value:
                return 'float'
            elif node.value.isdigit() or (node.value[0] == '-' and node.value[1:].isdigit()):
                return 'int'
            else:
                return 'string'
        elif node.node_type == 'identifier':
            if node.value in self.symbols:
                return self.symbols[node.value]['type']
            else:
                self._error(f"Undefined variable '{node.value}'", node)
                return 'int'  # Default fallback
        elif node.node_type == 'binary_expression':
            left_type = self._get_expression_type(node.children[0])
            right_type = self._get_expression_type(node.children[1])
            
            # Type promotion rules
            if 'string' in [left_type, right_type]:
                return 'string'
            elif 'float' in [left_type, right_type]:
                return 'float'
            elif 'int' in [left_type, right_type]:
                return 'int'
            else:
                return 'bool'
        
        return 'int'  # Default type
    
    def _error(self, message, node):
        self.errors.append(f"Line {node.line}: {message}")