
class Token:
    def __init__(self, ttype, value, line):
        self.ttype = ttype
        self.value = value
        self.line = line

def lex_file(path, token_defs):
    tokens = []
    with open(path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, 1):
            line = line.strip()
            if line.startswith("print"):
                # ambil seluruh string setelah print
                rest = line[len("print"):].strip()
                tokens.append(Token("print", rest, idx))
            elif line:
                tokens.append(Token("unknown", line, idx))
    return tokens
