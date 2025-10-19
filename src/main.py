# from token_reader import read_token_defs   <-- hapus ini
from lexer import lex_file
from parser import parse
from runner import run
import os

def main():
    root = os.getcwd()
    pyc_file = os.path.join(root, "examples", "hello.pyc")
    tokens = lex_file(pyc_file, [])  # token_defs tidak dipakai
    ast = parse(tokens)
    run(ast)

if __name__ == "__main__":
    main()
