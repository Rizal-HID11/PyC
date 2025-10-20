# PyC
PyC is a compiled programming language that combines Python-like simplicity with C-style block structure. Designed for ease of learning while maintaining high performance

This Language is still at Alpha Version it may not have complete syntax or complete systems.
Each Update may change some syntax because this still Aplpha Version.

**Current Versions: 0.9.0.1**

# TODO

Here some Tutorial:

- **To Execute the PyC Code** You must type "python src/main.py" in the Terminal it should be give output from files in examples/hello.pyc.

- **To type code the PyC Code** You must go to files in examples/hello.pyc then start type code that the syntax specific like PyC or while you execute it will error or not give the right output.

- **To type PyC Code** You must go to examples/hello.pyc and start typing PyC Code there

- **To Rename PyC Code Files** You must go to files src/main.py and go the last line then you see "compile_and_run("examples/hello.pyc") change hello.pyc to your hello.pyc new name you just change

---

# What's New?

**The Difference/New in this Version is:**

- **Calculations:** Now added Arithmetic Operator Syntax (like =>, =<, /)
- **Flexibility:** Now you can print but called variabel for example "print(Message)"
- **Variabel:** Now while making variabel can used for like number for math calculations
- **Complete:** Now Variables types is now complete (bool,int,string,float)
- **New Folder:** Added New Folder ``bin``

---

**What System You Can Make:**

**I will give a example code for some systems:**

**Simple Arithmetic Operations:**
```pyc
func main() {
    int x = 12
    int y = 14
    int result = y + x
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
    int x = 1
    int y = 2
    int result = x + y
    print(result)
}
```

---

# Syntax Directory

```json
[
  {"type": "keyword", "value": "func"},
  {"type": "keyword", "value": "return"},
  {"type": "keyword", "value": "print"},
  {"type": "keyword", "value": "if"},
  {"type": "keyword", "value": "else"},
  {"type": "keyword", "value": "while"},
  {"type": "keyword", "value": "class"},
  {"type": "keyword", "value": "new"},
  {"type": "keyword", "value": "this"},
  {"type": "type", "value": "int"},
  {"type": "type", "value": "float"},
  {"type": "type", "value": "string"},
  {"type": "type", "value": "bool"},
  {"type": "symbol", "value": "("},
  {"type": "symbol", "value": ")"},
  {"type": "symbol", "value": "{"},
  {"type": "symbol", "value": "}"},
  {"type": "symbol", "value": "["},
  {"type": "symbol", "value": "]"},
  {"type": "symbol", "value": ";"},
  {"type": "symbol", "value": ","},
  {"type": "symbol", "value": "."},
  {"type": "operator", "value": "="},
  {"type": "operator", "value": "+"},
  {"type": "operator", "value": "-"},
  {"type": "operator", "value": "*"},
  {"type": "operator", "value": "/"},
  {"type": "operator", "value": "=="},
  {"type": "operator", "value": "!="},
  {"type": "operator", "value": ">"},
  {"type": "operator", "value": "<"},
  {"type": "operator", "value": ">="},
  {"type": "operator", "value": "<="},
  {"type": "operator", "value": "!"},
  {"type": "boolean", "value": "true"},
  {"type": "boolean", "value": "false"}
]
```

---

# Short Explain

## Syntax ``func`` is To define a function
## Syntax ``print`` is To print text to the output (print only text not string variabel it won't work)
## Syntax ``int`` is To define a integer variabel
## Syntax  ``if`` is To define a if a action then what action should do 

---

# Project Structure

```text
pyc/
├── src/
│   ├── lexer.py          # Lexical analyzer
│   ├── parser.py         # Syntax parser
│   ├── compiler/         # Bytecode compiler
│   │   └── bytecode.py
│   │   └── semantic.py
│   ├── vm/               # Virtual machine
│   │   └── machine.py
│   ├── helper/               # Helper Functions
│   │   └── token_reader.py
│   └── main.py           # Main compiler driver
├── examples/             # Example PyC programs
│   ├── hello.pyc
└── assets/
    └── lists_tokens.json # Token definitions
```

**Stay tuned for more PyC updates! They're is still growing**
