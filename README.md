# PyC
PyC is a compiled programming language that combines Python-like simplicity with C-style block structure. Designed for ease of learning while maintaining high performance

This Language is still at Alpha Version it may not have complete syntax or complete systems.
Each Update may change some syntax because this still Aplpha Version.

**Do NOT rename or delete the file hello.pyc because it where you execute the code and the system compile then run it.**

# TODO

**To Execute the PyC Code** You must type "python src/main.py" in the Terminal it should be give output from files in examples/hello.pyc.

**To type code the PyC Code** You must go to files in examples/hello.pyc then start type code that the syntax specific like PyC or while you execute it will error or not give the right output.

# Example Code

```pyc
func main() {
    print "Hello, PyC!"
}
```

---

# Syntax Directory

In this version, The PyC Language is not have much Syntax.
He only can do:
- **Define Variabel**
- **Print To Output**

```json
{
[
  {"type": "keyword", "value": "func"},
  {"type": "keyword", "value": "print"},
  {"type": "symbol", "value": "("},
  {"type": "symbol", "value": ")"},
  {"type": "symbol", "value": "{"},
  {"type": "symbol", "value": "}"},
  {"type": "symbol", "value": ";"},
  {"type": "type", "value": "int"},
  {"type": "type", "value": "float"},
  {"type": "type", "value": "string"},
  {"type": "operator", "value": "="}
]
```

# Short Explain

Syntax **func** is To define a function

Syntax **print** is To print text to the output (print only text not string variabel it won't work)

Syntax **int** is To define a integer variabel

Syntax **float** To define decimal number variabel

Syntax **string** is To define a text variabel

---
