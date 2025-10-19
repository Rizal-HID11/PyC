from parser import parse
from runner import run
import os
from token_reader import read_token_defs


def main():
    root = os.getcwd()
    pyc_file = os.path.join(root, "examples", "hello.pyc")
    tokens = lex_file(pyc_file, [])
    ast = parse(tokens)
    run(ast)

if __name__ == "__main__":
    main()
