from lexer import tokenize

code = """
if (true) {
    print("THIS SHOULD PRINT")
}
"""

print("=== TOKEN DEBUG ===")
tokens = list(tokenize(code))
for i, token in enumerate(tokens):
    print(f"{i}: {token}")

# Cari token 'if'
if_tokens = [i for i, t in enumerate(tokens) if t[0] == 'IF' or t[1] == 'if']
print(f"IF tokens found: {if_tokens}")