# src/helper/token_reader.py
import json
import os

def read_token_defs():
    """Read token definitions from JSON file"""
    token_path = os.path.join(os.getcwd(), "assets", "lists_tokens.json")
    try:
        with open(token_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Token definitions not found: {token_path}")
        return []
    except json.JSONDecodeError:
        print(f"❌ Invalid JSON in token definitions")
        return []
from token_reader import read_token_defs  # Function to load token definitions


def main():
    root = os.getcwd()                       # Get current working directory
    pyc_file = os.path.join(root, "examples", "hello.pyc")  # Path to example file
    tokens = lex_file(pyc_file, [])          # Tokenize the file
    ast = parse(tokens)                      # Parse tokens into AST
    run(ast)                                 # Execute the AST

if __name__ == "__main__":
    main()                                   # Entry point of the program