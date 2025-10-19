# PyC
PyC is a compiled programming language that combines Python-like simplicity with C-style block structure. Designed for ease of learning while maintaining high performance

This Language is still at Alpha Version it may not have complete syntax or complete systems.
Each Update may change some syntax because this still Aplpha Version.

# TODO

Here some Tutorial:

- **To Execute the PyC Code** You must type "python src/main.py" in the Terminal it should be give output from files in examples/hello.pyc.

- **To type code the PyC Code** You must go to files in examples/hello.pyc then start type code that the syntax specific like PyC or while you execute it will error or not give the right output.

- **To type PyC Code** You must go to examples/hello.pyc and start typing PyC Code there

- **To Rename PyC Code Files** You must go to files src/main.py and go the last line then you see "compile_and_run("examples/hello.pyc") change hello.pyc to your hello.pyc new name you just change

---

# What's New?

**The new is:**

- **Calculations:** Now added Arithmetic Operator Syntax
- **Flexibility:** Now you can print but called variabel for example "print(Message)"
- **Variabel:** Now while making variabel can used for like number for math calculations

---

**What System You Can Make:**

**I will give a example code for some systems:**

**Arithmetic Operations:**
```pyc
func main() {
    float x = 12
    float y = 14
    float result = y+x
    print(result)
}
```
**Output: 26**

**Printings Something:**
```pyc
func main() {
    string Text = "Type Your Text Here"
    print(Text)
}
```
**Output: Type Your Text Here**

---

# Example Code

```pyc
func main() {
    float x = 1
    float y = 2
    float result = x + y
    print(result)
}
```

---

# Syntax Directory

**syntax = func, type = keyword**
**purpose: to make a functions**

**syntax = print, type = keyword**
**purpose: to print a text to the output**

**syntax = int, type = type**
**purpose: to make a integer variabel**

**syntax = float, type = type**
**purpose: to make a decimal number variabel**

**syntax string, type = type**
**purpose: to make a text variabel**

---

# Project Structure

```text
pyc/
├── src/
│   ├── lexer.py          # Lexical analyzer
│   ├── parser.py         # Syntax parser
│   ├── compiler/         # Bytecode compiler
│   │   └── bytecode.py
│   ├── vm/               # Virtual machine
│   │   └── machine.py
│   └── main.py           # Main compiler driver
├── examples/             # Example PyC programs
│   ├── hello.pyc
│   ├── calculator.pyc
│   ├── classes.pyc
│   └── loops.pyc
└── assets/
    └── lists_tokens.json # Token definitions
```

**Stay tuned for more PyC updates! They're is still growing**