# src/lexer.py
import re
from typing import Iterator, Tuple

def tokenize(code: str) -> Iterator[Tuple[str, str, int]]:
    patterns = [
        (r'\bfunc\b', 'FUNC'),
        (r'\breturn\b', 'RETURN'),
        (r'\bprint\b', 'PRINT'),
        (r'\bif\b', 'IF'),          
        (r'\belse\b', 'ELSE'),      
        (r'\b(int|float|string|bool)\b', 'TYPE'),
        (r'[a-zA-Z_]\w*', 'IDENT'),
        (r'\d+\.?\d*', 'NUMBER'),
        (r'"[^"]*"', 'STRING'),
        (r'[+\-*/]', 'OP'),
        (r'[=!]=|[<>]=?', 'COMPARE'),
        (r'=', 'ASSIGN'),
        (r'[(){},;]', 'PUNCT'),
        (r'\s+', None),
]
    
    line = 1
    pos = 0
    
    while pos < len(code):
        for pattern, tag in patterns:
            if match := re.match(pattern, code[pos:]):
                text = match.group()
                if tag:
                    yield (tag, text, line)
                line += text.count('\n')
                pos += len(text)
                break
        else:
            # Skip unknown characters instead of crashing
            pos += 1