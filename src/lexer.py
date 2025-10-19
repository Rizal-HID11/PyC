# src/lexer.py
import re
from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class Token:
    type: str
    value: str
    line: int

def tokenize(code: str) -> List[Token]:
    patterns = [
        (r'\b(func|return|print|if|else|while)\b', 'KEYWORD'),
        (r'\b(int|float|string|bool)\b', 'TYPE'),
        (r'[a-zA-Z_]\w*', 'IDENT'),
        (r'\d+\.?\d*', 'NUMBER'),
        (r'"[^"]*"', 'STRING'),
        (r'[+\-*/]=?|[=!]=?|[<>]=?', 'OP'),
        (r'[(){},;]', 'PUNCT'),
        (r'\s+', None)
    ]
    
    tokens = []
    line = 1
    pos = 0
    
    while pos < len(code):
        for pattern, tag in patterns:
            if match := re.match(pattern, code[pos:]):
                text = match.group()
                if tag:
                    tokens.append(Token(tag, text, line))
                line += text.count('\n')
                pos += len(text)
                break
        else:
            pos += 1  # Skip invalid chars
    
    return tokens