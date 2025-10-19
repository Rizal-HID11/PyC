from parser import parse
from runner import run
import os
from token_reader import read_token_defs  # Function to load token definitions


def main():
    root = os.getcwd()                       # Get current working directory
    pyc_file = os.path.join(root, "examples", "hello.pyc")  # Path to example file
    tokens = lex_file(pyc_file, [])          # Tokenize the file
    ast = parse(tokens)                      # Parse tokens into AST
    run(ast)                                 # Execute the AST

if __name__ == "__main__":
    main()                                   # Entry point of the program
