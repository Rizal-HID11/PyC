class Token:
    def __init__(self, ttype, value, line):
        self.ttype = ttype      # Type of token
        self.value = value      # Token value
        self.line = line        # Line number in file

def lex_file(path, token_defs):
    tokens = []                # List to store tokens
    with open(path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, 1):
            line = line.strip()
            if line.startswith("print"):
                # Capture content after 'print'
                rest = line[len("print"):].strip()
                tokens.append(Token("print", rest, idx))
            elif line:
                tokens.append(Token("unknown", line, idx))  # Unknown token
    return tokens
