# 1. VARIABLES & DATA TYPES 📦
# Numbers & Basic Math
```python
# === INTEGER & FLOAT ===
umur = 25
harga_bakso = 15000.50

print(f"Umur: {umur}")           # 25
print(f"Harga bakso: {harga_bakso}")  # 15000.5

# === OPERASI MATEMATIKA ===
gaji_bulanan = 10000000
bonus = 2500000
pajak = 0.1

gaji_bersih = gaji_bulanan + bonus - (gaji_bulanan * pajak)
print(f"Gaji bersih: Rp {gaji_bersih:,}")  # Rp 11,250,000.0

# === PEMBULATAN ===
harga_produk = 19999.99
print(f"Harga bulat: Rp {round(harga_produk)}")  # Rp 20000

nilai_rata_rata = 85.6789
print(f"Nilai: {round(nilai_rata_rata, 1)}")  # 85.7
```

# Strings (Text)
```python
# === STRING DASAR ===
nama = "Budi"
pekerjaan = "Programmer"

print(f"Nama: {nama}")        # Budi
print(f"Pekerjaan: {pekerjaan}")  # Programmer

# === STRING OPERATIONS ===
alamat = "Jl. Merdeka No. 123"
print(alamat.upper())     # JL. MERDEKA NO. 123
print(alamat.lower())     # jl. merdeka no. 123
print(alamat.title())     # Jl. Merdeka No. 123

# === CEK STRING ===
email = "budi@gmail.com"
print("@gmail.com" in email)  # True
print(email.startswith("budi"))  # True
Booleans & Comparisons
python
# === COMPARISON ===
uang_dompet = 50000
harga_laptop = 15000000

cukup_uang = uang_dompet >= harga_laptop
print(f"Cukup beli laptop? {cukup_uang}")  # False

# === LOGICAL OPERATORS ===
punya_ktp = True
umur = 20

bisa_buat_rekening = punya_ktp and umur >= 17
print(f"Bisa buat rekening: {bisa_buat_rekening}")  # True
```

# 2. LISTS & LOOPS 🔄
# Lists (Arrays)
```python
# === LIST DASAR ===
buah = ["apel", "mangga", "jeruk", "anggur"]
harga = [15000, 12000, 8000, 25000]

print(buah[0])    # apel
print(harga[-1])  # 25000 (item terakhir)

# === OPERASI LIST ===
buah.append("durian")      # Tambah di akhir
buah.insert(1, "nanas")   # Sisip di index 1

buah.remove("jeruk")       # Hapus jeruk
item_dihapus = buah.pop()  # Hapus item terakhir

print(buah)  # ['apel', 'nanas', 'mangga', 'anggur']
```

# Loops
```python
# === FOR LOOP DASAR ===
buah = ["apel", "mangga", "jeruk"]
harga = [15000, 12000, 8000]

# Loop biasa
for nama_buah in buah:
    print(f"Buah: {nama_buah}")

# Loop dengan index
for i in range(len(buah)):
    print(f"{buah[i]} = Rp {harga[i]:,}")

# Output:
# apel = Rp 15,000
# mangga = Rp 12,000  
# jeruk = Rp 8,000

# === WHILE LOOP ===
saldo = 100000
tarikan = 25000

while saldo > 0:
    print(f"Saldo: Rp {saldo:,}")
    saldo -= tarikan
    if saldo < tarikan:
        print("Saldo hampir habis!")
        break
```

# 3. FUNCTIONS 🛠️
Basic Functions
```python
# === FUNCTION SEDERHANA ===
def hitung_total(harga, jumlah):
    """Hitung total harga belanja"""
    total = harga * jumlah
    return total

# Pakai function
total_bayar = hitung_total(15000, 3)
print(f"Total: Rp {total_bayar:,}")  # Total: Rp 45,000

# === FUNCTION DENGAN DEFAULT VALUE ===
def sapa(nama, waktu="pagi"):
    """Sapa seseorang"""
    return f"Selamat {waktu}, {nama}!"

print(sapa("Budi"))              # Selamat pagi, Budi!
print(sapa("Ani", "siang"))      # Selamat siang, Ani!
```

# Lambda (Simple Functions)
```python
# === LAMBDA UNTUK OPERASI SEDERHANA ===
kali_dua = lambda x: x * 2
print(kali_dua(10))  # 20

# Pakai di map()
angka = [1, 2, 3, 4, 5]
hasil = list(map(lambda x: x * 2, angka))
print(hasil)  # [2, 4, 6, 8, 10]
```

4. CONDITIONALS (IF/ELSE) 🤔
```python
# === IF/ELIF/ELSE ===
nilai = 85

if nilai >= 90:
    grade = "A"
    print("Luar biasa!")
elif nilai >= 80:
    grade = "B" 
    print("Bagus!")
elif nilai >= 70:
    grade = "C"
    print("Cukup!")
else:
    grade = "D"
    print("Remedial!")

print(f"Grade: {grade}")  # Grade: B

# === CONDITIONAL REAL-WORLD ===
umur = 20
punya_sim = True

if umur >= 17 and punya_sim:
    print("Boleh nyetir mobil")
else:
    print("Gak boleh nyetir!")
```

5. DICTIONARIES (KEY-VALUE) 📖
```python
# === DICTIONARY DASAR ===
mahasiswa = {
    "nama": "Budi Santoso",
    "nim": "123456",
    "jurusan": "Informatika",
    "ipk": 3.75
}

# Akses data
print(mahasiswa["nama"])     # Budi Santoso
print(mahasiswa.get("nim"))  # 123456

# Update data
mahasiswa["ipk"] = 3.80
mahasiswa["semester"] = 5    # Tambah key baru

# Loop through dictionary
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

# Output:
# nama: Budi Santoso
# nim: 123456  
# jurusan: Informatika
# ipk: 3.8
# semester: 5
```

6. FILE HANDLING 📁
```python
# === BACA FILE ===
with open("data.txt", "r") as file:
    isi_file = file.read()
    print(isi_file)

# === TULIS FILE ===
data_mahasiswa = ["Budi,90,85", "Ani,95,88", "Citra,87,92"]

with open("nilai.txt", "w") as file:
    for data in data_mahasiswa:
        file.write(data + "\n")

# === BACA PER BARIS ===
with open("nilai.txt", "r") as file:
    for line in file:
        nama, nilai1, nilai2 = line.strip().split(",")
        print(f"{nama}: {nilai1}, {nilai2}")
```

7. ERROR HANDLING 🚨
```python
# === TRY/EXCEPT DASAR ===
try:
    angka = int(input("Masukkan angka: "))
    hasil = 100 / angka
    print(f"Hasil: {hasil}")
except ValueError:
    print("Error: Input harus angka!")
except ZeroDivisionError:
    print("Error: Tidak bisa bagi dengan nol!")
except Exception as e:
    print(f"Error tak terduga: {e}")
else:
    print("Perhitungan berhasil!")
finally:
    print("Program selesai dijalankan")
```

8. USEFUL BUILT-IN FUNCTIONS ⚡
Type Conversion
```python
# === KONVERSI TIPE DATA ===
teks_angka = "100"
angka = int(teks_angka)      # 100
float_angka = float("3.14")  # 3.14
string_angka = str(123)      # "123"

print(f"Hasil: {angka + 50}")  # 150
Useful Functions
python
# === LEN() - PANJANG DATA ===
nama = "Budi Santoso"
print(len(nama))  # 12

buah = ["apel", "mangga", "jeruk"]
print(len(buah))  # 3

# === RANGE() - GENERATE ANGKA ===
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# === ENUMERATE() - LOOP DENGAN INDEX ===
buah = ["apel", "mangga", "jeruk"]
for index, nama_buah in enumerate(buah):
    print(f"{index + 1}. {nama_buah}")

# Output:
# 1. apel
# 2. mangga  
# 3. jeruk
```

9. CLASSES & OBJECTS 🏗️
```python
# === CLASS DASAR ===
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.nilai = []
    
    def tambah_nilai(self, nilai):
        self.nilai.append(nilai)
    
    def rata_rata(self):
        if self.nilai:
            return sum(self.nilai) / len(self.nilai)
        return 0
    
    def info(self):
        return f"{self.nama} (NIM: {self.nim}) - IPK: {self.rata_rata():.2f}"

# Pakai class
mhs1 = Mahasiswa("Budi Santoso", "123456")
mhs1.tambah_nilai(85)
mhs1.tambah_nilai(90)
mhs1.tambah_nilai(78)

print(mhs1.info())  # Budi Santoso (NIM: 123456) - IPK: 84.33
```

10. REAL-WORLD EXAMPLE 🌟
```python
# === SISTEM TOKO SEDERHANA ===

# Data produk
produk = {
    "bakso": 15000,
    "mie ayam": 12000, 
    "es teh": 5000,
    "nasi goreng": 18000
}

# Fungsi hitung total
def hitung_pesanan(pesanan):
    total = 0
    print("=== STRUK PEMBAYARAN ===")
    
    for item, jumlah in pesanan.items():
        if item in produk:
            harga_total = produk[item] * jumlah
            total += harga_total
            print(f"{item:12} {jumlah} x Rp {produk[item]:,} = Rp {harga_total:,}")
    
    print(f"{'TOTAL':12} {'':11} Rp {total:,}")
    return total

# Contoh pemakaian
pesanan_saya = {
    "bakso": 2,
    "es teh": 3, 
    "nasi goreng": 1
}

hitung_pesanan(pesanan_saya)

# Output:
# === STRUK PEMBAYARAN ===
# bakso        2 x Rp 15,000 = Rp 30,000
# es teh       3 x Rp 5,000 = Rp 15,000  
# nasi goreng  1 x Rp 18,000 = Rp 18,000
# TOTAL                    Rp 63,000
```


## BONUS: PYTHON SHORTCUTS 🎯
```python
# === LIST COMPREHENSION ===
# Cara biasa:
angka = [1, 2, 3, 4, 5]
kuadrat = []
for x in angka:
    kuadrat.append(x * x)

# Cara Pythonic:
kuadrat = [x * x for x in angka]  # [1, 4, 9, 16, 25]

# === TERNARY OPERATOR ===
umur = 20
status = "Dewasa" if umur >= 18 else "Anak-anak"

# === MULTIPLE ASSIGNMENT ===
nama, umur, kota = "Budi", 25, "Jakarta"
```


























## ISI KODE ##

parser.py
# src/parser.py
from typing import List, Optional
from dataclasses import dataclass

@dataclass
class AST:
    type: str
    value: str = ""
    children: List['AST'] = None
    
    def __post_init__(self):
        if self.children is None:
            self.children = []

class Parser:
    def __init__(self, tokens: List[tuple]):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[0] if tokens else None
    
    def eat(self, token_type: str = None, value: str = None) -> tuple:
        if not self.current_token:
            raise SyntaxError("Unexpected end of input")
        
        if token_type and self.current_token[0] != token_type:
            raise SyntaxError(f"Expected {token_type}, got {self.current_token[0]}")
        
        if value and self.current_token[1] != value:
            raise SyntaxError(f"Expected '{value}', got '{self.current_token[1]}'")
        
        token = self.current_token
        self.pos += 1
        self.current_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None
        return token

    def peek(self) -> Optional[tuple]:
        return self.current_token

    def parse(self) -> AST:
        statements = []
        
        while self.current_token:
            try:
                if self.current_token[0] == 'FUNC':
                    stmt = self.parse_function()
                elif self.current_token[0] == 'PRINT':
                    stmt = self.parse_print()
                elif self.current_token[0] == 'TYPE':
                    stmt = self.parse_var_decl()
                elif self.current_token[0] == 'IDENT':
                    next_token = self.tokens[self.pos + 1] if self.pos + 1 < len(self.tokens) else None
                    if next_token and next_token[1] == '(':
                        stmt = self.parse_function_call()
                    elif next_token and next_token[0] == 'ASSIGN':
                        stmt = self.parse_assignment()
                    else:
                        self.eat()
                        continue
                else:
                    self.eat()
                    continue
                
                if stmt:
                    statements.append(stmt)
                    
            except Exception as e:
                print(f"Parser error: {e}")
                # Skip to next potential statement
                self.pos += 1
                self.current_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None
        
        return AST('Program', children=statements)
    
    def parse_function(self) -> AST:
        self.eat('FUNC')
        name = self.eat('IDENT')[1]
        self.eat('PUNCT', '(')
        self.eat('PUNCT', ')')
        
        return_type = None
        if self.current_token and self.current_token[0] == 'TYPE':
            return_type = self.eat('TYPE')[1]
        
        self.eat('PUNCT', '{')
        
        body = []
        while self.current_token and self.current_token[1] != '}':
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
        
        self.eat('PUNCT', '}')
        
        return AST('Function', f"{name}:{return_type}" if return_type else name, body)
    
    def parse_statement(self) -> AST:
        if not self.current_token:
            return None
            
        if self.current_token[0] == 'PRINT':
            return self.parse_print()
        elif self.current_token[0] == 'TYPE':
            return self.parse_var_decl()
        elif self.current_token[0] == 'IDENT':
            next_token = self.tokens[self.pos + 1] if self.pos + 1 < len(self.tokens) else None
            if next_token and next_token[1] == '(':
                return self.parse_function_call()
            elif next_token and next_token[0] == 'ASSIGN':
                return self.parse_assignment()
        elif self.current_token[0] == 'RETURN':
            return self.parse_return()
        
        # Skip unknown
        self.eat()
        return None
    
    def parse_print(self) -> AST:
        self.eat('PRINT')
        self.eat('PUNCT', '(')
        expr = self.parse_expression()
        self.eat('PUNCT', ')')
        return AST('Print', children=[expr])
    
    def parse_return(self) -> AST:
        self.eat('RETURN')
        expr = self.parse_expression() if self.current_token and self.current_token[0] != 'PUNCT' else None
        return AST('Return', children=[expr] if expr else [])
    
    def parse_var_decl(self) -> AST:
        var_type = self.eat('TYPE')[1]
        name = self.eat('IDENT')[1]
        
        init = None
        if self.current_token and self.current_token[0] == 'ASSIGN':
            self.eat('ASSIGN')
            init = self.parse_expression()
        
        return AST('VarDecl', f"{name}:{var_type}", [init] if init else [])
    
    def parse_assignment(self) -> AST:
        name = self.eat('IDENT')[1]
        self.eat('ASSIGN')
        value = self.parse_expression()
        return AST('Assign', name, [value])
    
    def parse_function_call(self) -> AST:
        name = self.eat('IDENT')[1]
        self.eat('PUNCT', '(')
        
        args = []
        while self.current_token and self.current_token[1] != ')':
            args.append(self.parse_expression())
            if self.current_token and self.current_token[1] == ',':
                self.eat('PUNCT', ',')
        
        self.eat('PUNCT', ')')
        return AST('Call', name, args)
    
    def parse_expression(self) -> AST:
        left = self.parse_term()
        
        while self.current_token and self.current_token[0] in ['OP', 'COMPARE']:
            op = self.eat()[1]
            right = self.parse_term()
            left = AST('BinaryOp', op, [left, right])
        
        return left
    
    def parse_term(self) -> AST:
        left = self.parse_factor()
        
        while self.current_token and self.current_token[0] == 'OP' and self.current_token[1] in ['*', '/']:
            op = self.eat()[1]
            right = self.parse_factor()
            left = AST('BinaryOp', op, [left, right])
        
        return left
    
    def parse_factor(self) -> AST:
        if not self.current_token:
            raise SyntaxError("Unexpected end in expression")
        
        token = self.current_token
        
        if token[0] == 'IDENT':
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][1] == '(':
                return self.parse_function_call()
            else:
                return AST('Variable', self.eat('IDENT')[1])
        elif token[0] == 'NUMBER':
            return AST('Number', self.eat('NUMBER')[1])
        elif token[0] == 'STRING':
            value = self.eat('STRING')[1][1:-1]  # Remove quotes
            return AST('String', value)
        elif token[1] == '(':
            self.eat('PUNCT', '(')
            expr = self.parse_expression()
            self.eat('PUNCT', ')')
            return expr
        else:
            raise SyntaxError(f"Unexpected token in expression: {token[1]}")

def parse(tokens: List[tuple]) -> AST:
    return Parser(tokens).parse()
lexer.py

# src/lexer.py
import re
from typing import Iterator, Tuple

def tokenize(code: str) -> Iterator[Tuple[str, str, int]]:
    patterns = [
        (r'\bfunc\b', 'FUNC'),
        (r'\breturn\b', 'RETURN'),
        (r'\bprint\b', 'PRINT'),
        (r'\bif\b', 'IF'),          
        (r'\belse\b', 'ELSE'),      
        (r'\b(int|float|string|bool)\b', 'TYPE'),
        (r'[a-zA-Z_]\w*', 'IDENT'),
        (r'\d+\.?\d*', 'NUMBER'),
        (r'"[^"]*"', 'STRING'),
        (r'[+\-*/]', 'OP'),
        (r'[=!]=|[<>]=?', 'COMPARE'),
        (r'=', 'ASSIGN'),
        (r'[(){},;]', 'PUNCT'),
        (r'\s+', None),
]
    
    line = 1
    pos = 0
    
    while pos < len(code):
        for pattern, tag in patterns:
            if match := re.match(pattern, code[pos:]):
                text = match.group()
                if tag:
                    yield (tag, text, line)
                line += text.count('\n')
                pos += len(text)
                break
        else:
            # Skip unknown characters instead of crashing
            pos += 1
lists_tokens.json
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
  {"type": "type", "value": "void"},
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
main.py

# src/main.py
from lexer import tokenize
from parser import parse
from compiler.bytecode import Compiler
from vm.machine import VM

def compile_and_run(source_file: str):
    print(f"🚀 Modern PyC - {source_file}")
    
    with open(source_file, 'r') as f:
        source = f.read()
    
    print("📝 Source:")
    print(source)
    print()
    
    # Lex
    tokens = list(tokenize(source))
    print(f"✅ Tokens: {len(tokens)}")
    
    # Parse
    try:
        ast = parse(tokens)
        print(f"✅ AST: {ast.type} with {len(ast.children)} children")
        
        # DEBUG: Print AST structure
        if ast.children:
            print("🌳 AST Structure:")
            for i, child in enumerate(ast.children):
                print(f"   {i}: {child.type} '{child.value}' with {len(child.children)} children")
        else:
            print("❌ WARNING: AST has no children!")
            
    except Exception as e:
        print(f"❌ Parser Error: {e}")
        return
    
    # Compile
    compiler = Compiler()
    bytecode = compiler.compile(ast)
    
    # Execute
    print("🚀 Execution:")
    print("-" * 30)
    vm = VM()
    vm.load(bytecode)
    vm.run()
    print("-" * 30)

if __name__ == "__main__":
    compile_and_run("examples/hello.pyc")
machine.py

# src/vm/machine.py
import struct
from compiler.bytecode import OpCode

class VM:
    def __init__(self):
        self.stack = []
        self.vars = [None] * 100
        self.constants = []
        self.code = []
        self.pc = 0
        self.call_stack = []
    
    def load(self, bytecode: bytes):
        if bytecode[:4] != b'PYBC':
            raise Exception("Invalid bytecode")
        
        pos = 5
        
        # Constants
        const_count = struct.unpack('H', bytecode[pos:pos+2])[0]
        pos += 2
        
        self.constants = []
        for _ in range(const_count):
            const_type = bytecode[pos]
            pos += 1
            
            if const_type == 1:  # String
                length = struct.unpack('H', bytecode[pos:pos+2])[0]
                pos += 2
                value = bytecode[pos:pos+length].decode('utf-8')
                pos += length
                self.constants.append(value)
            elif const_type == 2:  # Integer
                value = struct.unpack('i', bytecode[pos:pos+4])[0]
                pos += 4
                self.constants.append(value)
            elif const_type == 3:  # Float
                value = struct.unpack('d', bytecode[pos:pos+8])[0]
                pos += 8
                self.constants.append(value)
        
        # Code
        code_count = struct.unpack('I', bytecode[pos:pos+4])[0]
        pos += 4
        
        self.code = []
        for _ in range(code_count):
            opcode = bytecode[pos]
            operand = struct.unpack('i', bytecode[pos+1:pos+5])[0]
            pos += 5
            self.code.append((opcode, operand))
        
        print(f"✅ VM loaded: {len(self.constants)} constants, {len(self.code)} instructions")
    
    def run(self):
        self.pc = 0
        self.stack = []
        self.call_stack = []
        
        print("🚀 VM Execution Started")
        
        try:
            while self.pc < len(self.code):
                op, arg = self.code[self.pc]
                self.execute(OpCode(op), arg)
                self.pc += 1
        except Exception as e:
            print(f"❌ VM Error at instruction {self.pc}: {e}")
            raise
        
        print("✅ VM Execution Finished")
    
    def execute(self, opcode: OpCode, arg: int):
        try:
            if opcode == OpCode.LOAD_CONST:
                self.stack.append(self.constants[arg])
            
            elif opcode == OpCode.LOAD_VAR:
                self.stack.append(self.vars[arg])
            
            elif opcode == OpCode.STORE_VAR:
                self.vars[arg] = self.stack.pop()
            
            elif opcode == OpCode.POP:
                self.stack.pop()
            
            # Arithmetic operations
            elif opcode == OpCode.ADD:
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a + b)
            
            elif opcode == OpCode.SUB:
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a - b)
            
            elif opcode == OpCode.MUL:
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a * b)
            
            elif opcode == OpCode.DIV:
                b, a = self.stack.pop(), self.stack.pop()
                if b == 0:
                    raise Exception("Division by zero!")
                self.stack.append(a / b)
            
            # Comparison operations
            elif opcode == OpCode.EQ:
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a == b)
            
            elif opcode == OpCode.NEQ:
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a != b)
            
            elif opcode == OpCode.GT:
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a > b)
            
            elif opcode == OpCode.LT:
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a < b)
            
            elif opcode == OpCode.GTE:
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a >= b)
            
            elif opcode == OpCode.LTE:
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a <= b)
            
            # Control flow
            elif opcode == OpCode.JUMP:
                self.pc = arg - 1  # -1 because we increment after
            
            elif opcode == OpCode.JUMP_IF_FALSE:
                if not self.stack.pop():
                    self.pc = arg - 1
            
            elif opcode == OpCode.JUMP_IF_TRUE:
                if self.stack.pop():
                    self.pc = arg - 1
            
            elif opcode == OpCode.CALL:
                self.call_stack.append(self.pc)
                self.pc = arg - 1
            
            elif opcode == OpCode.RETURN:
                if self.call_stack:
                    self.pc = self.call_stack.pop()
                else:
                    self.pc = len(self.code)
            
            # Built-ins
            elif opcode == OpCode.PRINT:
                value = self.stack.pop()
                print(value)
            
            elif opcode == OpCode.HALT:
                self.pc = len(self.code)
            
            else:
                raise Exception(f"Unknown opcode: {opcode}")
                
        except Exception as e:
            raise Exception(f"Error executing {opcode}: {e}")
bytecode.py
# src/compiler/bytecode.py
from enum import Enum
import struct
from typing import Any, Dict, List

class OpCode(Enum):
    # Stack operations
    LOAD_CONST = 1
    LOAD_VAR = 2
    STORE_VAR = 3
    POP = 4
    
    # Arithmetic operations
    ADD = 10
    SUB = 11
    MUL = 12
    DIV = 13
    
    # Comparison operations
    EQ = 20
    NEQ = 21
    GT = 22
    LT = 23
    GTE = 24
    LTE = 25
    
    # Control flow
    JUMP = 30
    JUMP_IF_FALSE = 31
    JUMP_IF_TRUE = 32
    CALL = 33
    RETURN = 34
    
    # Built-ins
    PRINT = 40
    
    # Program control
    HALT = 255

class Compiler:
    def __init__(self):
        self.code = []
        self.constants = []
        self.variables = {}
        self.functions = {}
        self.labels = {}  # For jump targets
        self.label_counter = 0
    
    def compile(self, ast) -> bytes:
        print("🔧 Compilation Started")
        
        # Find all functions first
        for stmt in ast.children:
            if stmt.type == 'Function':
                func_name = stmt.value.split(':')[0] if ':' in stmt.value else stmt.value
                self.functions[func_name] = len(self.code)
                print(f"📍 Function '{func_name}' at position {len(self.code)}")
        
        # Compile all statements
        for stmt in ast.children:
            self.compile_statement(stmt)
        
        # Resolve all labels
        self.resolve_labels()
        
        # Add halt if needed
        if not self.code or self.code[-1][0] != OpCode.HALT.value:
            self.emit(OpCode.HALT)
        
        print(f"✅ Compilation Complete: {len(self.code)} instructions")
        return self.serialize()
    
    def compile_statement(self, stmt):
        if stmt.type == 'Function':
            self.compile_function(stmt)
        elif stmt.type == 'Print':
            self.compile_print(stmt)
        elif stmt.type == 'VarDecl':
            self.compile_var_decl(stmt)
        elif stmt.type == 'Assign':
            self.compile_assign(stmt)
        elif stmt.type == 'Call':
            self.compile_call(stmt)
        elif stmt.type == 'If':
            self.compile_if(stmt)
        elif stmt.type == 'ExprStmt':
            expr = stmt.children[0]
            if expr.type == 'Call':
                self.compile_call(expr)
            else:
                self.compile_expression(expr)
                self.emit(OpCode.POP)
    
    def compile_function(self, func):
        func_name = func.value.split(':')[0] if ':' in func.value else func.value
        print(f"🔨 Compiling function: {func_name}")
        
        # Save current state
        old_vars = self.variables.copy()
        self.variables = {}  # New scope
        
        # Update function position
        self.functions[func_name] = len(self.code)
        
        # Compile function body
        for stmt in func.children:
            self.compile_statement(stmt)
        
        # Add return if missing
        if not any(child.type == 'Return' for child in func.children):
            self.emit(OpCode.LOAD_CONST, self.add_constant(0))
            self.emit(OpCode.RETURN)
        
        # Restore state
        self.variables = old_vars
    
    def compile_print(self, stmt):
        self.compile_expression(stmt.children[0])
        self.emit(OpCode.PRINT)
    
    def compile_var_decl(self, stmt):
        var_name = stmt.value.split(':')[0]
        if var_name not in self.variables:
            self.variables[var_name] = len(self.variables)
        
        if stmt.children:  # Has initial value
            self.compile_expression(stmt.children[0])
            self.emit(OpCode.STORE_VAR, self.variables[var_name])
    
    def compile_assign(self, stmt):
        var_name = stmt.value
        if var_name not in self.variables:
            self.variables[var_name] = len(self.variables)
        
        self.compile_expression(stmt.children[0])
        self.emit(OpCode.STORE_VAR, self.variables[var_name])
    
    def compile_call(self, call):
        func_name = call.value
        
        if func_name not in self.functions:
            raise Exception(f"Undefined function: {func_name}")
        
        # Compile arguments
        for arg in call.children:
            self.compile_expression(arg)
        
        self.emit(OpCode.CALL, self.functions[func_name])
        self.emit(OpCode.POP)  # Discard return value
    
    def compile_if(self, stmt):
        # condition, then_block, else_block
        self.compile_expression(stmt.children[0])  # Condition
        
        else_label = self.new_label()
        end_label = self.new_label()
        
        # Jump to else if condition is false
        self.emit(OpCode.JUMP_IF_FALSE, else_label)
        
        # Compile then block
        for then_stmt in stmt.children[1].children:
            self.compile_statement(then_stmt)
        
        # Jump to end after then block
        self.emit(OpCode.JUMP, end_label)
        
        # Else block
        self.place_label(else_label)
        for else_stmt in stmt.children[2].children:
            self.compile_statement(else_stmt)
        
        self.place_label(end_label)
    
    def compile_expression(self, expr):
        if expr.type == 'String':
            const_idx = self.add_constant(expr.value)
            self.emit(OpCode.LOAD_CONST, const_idx)
        elif expr.type == 'Number':
            value = float(expr.value) if '.' in expr.value else int(expr.value)
            const_idx = self.add_constant(value)
            self.emit(OpCode.LOAD_CONST, const_idx)
        elif expr.type == 'Variable':
            if expr.value not in self.variables:
                raise Exception(f"Undefined variable: {expr.value}")
            self.emit(OpCode.LOAD_VAR, self.variables[expr.value])
        elif expr.type == 'BinaryOp':
            self.compile_binary_op(expr)
        elif expr.type == 'Call':
            self.compile_call(expr)
    
    def compile_binary_op(self, expr):
        # Compile left and right operands
        self.compile_expression(expr.children[0])
        self.compile_expression(expr.children[1])
        
        # Emit the operation
        op_map = {
            '+': OpCode.ADD,
            '-': OpCode.SUB,
            '*': OpCode.MUL,
            '/': OpCode.DIV,
            '==': OpCode.EQ,
            '!=': OpCode.NEQ,
            '>': OpCode.GT,
            '<': OpCode.LT,
            '>=': OpCode.GTE,
            '<=': OpCode.LTE
        }
        
        if expr.value in op_map:
            self.emit(op_map[expr.value])
        else:
            raise Exception(f"Unsupported operator: {expr.value}")
    
    def new_label(self):
        self.label_counter += 1
        return self.label_counter
    
    def place_label(self, label):
        self.labels[label] = len(self.code)
    
    def resolve_labels(self):
        """Replace label IDs with actual code positions"""
        resolved_code = []
        for opcode, operand in self.code:
            if opcode in [OpCode.JUMP.value, OpCode.JUMP_IF_FALSE.value, OpCode.JUMP_IF_TRUE.value]:
                # Replace label ID with actual position
                if operand in self.labels:
                    resolved_code.append((opcode, self.labels[operand]))
                else:
                    resolved_code.append((opcode, operand))
            else:
                resolved_code.append((opcode, operand))
        self.code = resolved_code
    
    def emit(self, opcode: OpCode, operand: int = 0):
        self.code.append((opcode.value, operand))
        print(f"   💾 {opcode.name} {operand}")
    
    def add_constant(self, value: Any) -> int:
        self.constants.append(value)
        return len(self.constants) - 1
    
    def serialize(self) -> bytes:
        result = bytearray(b'PYBC\x01')
        
        # Constants
        result.extend(struct.pack('H', len(self.constants)))
        for const in self.constants:
            if isinstance(const, str):
                result.append(1)
                encoded = const.encode('utf-8')
                result.extend(struct.pack('H', len(encoded)))
                result.extend(encoded)
            elif isinstance(const, int):
                result.append(2)
                result.extend(struct.pack('i', const))
            elif isinstance(const, float):
                result.append(3)
                result.extend(struct.pack('d', const))
        
        # Code
        result.extend(struct.pack('I', len(self.code)))
        for op, operand in self.code:
            result.append(op)
            result.extend(struct.pack('i', operand))
        
        return bytes(result)
semantic.py
# src/compiler/semantic.py
class SemanticAnalyzer:
    def __init__(self):
        self.symbols = {}  # {name: {'type': type, 'kind': 'variable|function'}}
        self.errors = []
        self.current_function = None
    
    def analyze(self, ast):
        self.symbols = {}
        self.errors = []
        self.current_function = None
        
        # Add built-in functions
        self.symbols['print'] = {'type': 'void', 'kind': 'function'}
        
        self._analyze_node(ast)
        return len(self.errors) == 0, self.errors
    
    def _analyze_node(self, node):
        method_name = f'_analyze_{node.node_type}'
        method = getattr(self, method_name, lambda n: None)
        method(node)
    
    def _analyze_program(self, node):
        for child in node.children:
            self._analyze_node(child)
    
    def _analyze_function(self, node):
        func_name = node.value
        
        if func_name in self.symbols:
            self._error(f"Function '{func_name}' already defined", node)
            return
        
        # Register function
        self.symbols[func_name] = {
            'type': node.data_type or 'void',
            'kind': 'function',
            'node': node
        }
        
        old_function = self.current_function
        old_symbols = self.symbols.copy()
        
        self.current_function = func_name
        
        # Analyze parameters
        for child in node.children:
            if child.node_type == 'parameter':
                param_name = child.value
                if param_name in self.symbols:
                    self._error(f"Parameter '{param_name}' already defined", child)
                else:
                    self.symbols[param_name] = {
                        'type': child.data_type,
                        'kind': 'variable'
                    }
        
        # Analyze function body
        for child in node.children:
            if child.node_type != 'parameter':
                self._analyze_node(child)
        
        self.current_function = old_function
        self.symbols = old_symbols
    
    def _analyze_variable_declaration(self, node):
        var_name = node.value
        
        if var_name in self.symbols:
            self._error(f"Variable '{var_name}' already declared", node)
            return
        
        self.symbols[var_name] = {
            'type': node.data_type,
            'kind': 'variable'
        }
        
        # Check initialization
        if node.children:
            self._check_assignment(node.data_type, node.children[0], node)
    
    def _analyze_assignment(self, node):
        var_name = node.value
        
        if var_name not in self.symbols:
            self._error(f"Undefined variable '{var_name}'", node)
            return
        
        var_info = self.symbols[var_name]
        
        if node.children:
            self._check_assignment(var_info['type'], node.children[0], node)
    
    def _analyze_function_call(self, node):
        func_name = node.value
        
        if func_name not in self.symbols:
            self._error(f"Undefined function '{func_name}'", node)
            return
        
        # TODO: Check argument types and count
        # For now, just verify function exists
    
    def _analyze_print_statement(self, node):
        if node.children:
            self._analyze_node(node.children[0])
    
    def _analyze_return_statement(self, node):
        if not self.current_function:
            self._error("Return statement outside function", node)
            return
        
        func_info = self.symbols[self.current_function]
        return_type = func_info['type']
        
        if node.children and return_type == 'void':
            self._error(f"Function '{self.current_function}' returns void but has return value", node)
        elif not node.children and return_type != 'void':
            self._error(f"Function '{self.current_function}' must return a value", node)
        elif node.children and return_type != 'void':
            # Check return type compatibility
            expr_type = self._get_expression_type(node.children[0])
            if expr_type != return_type and not (return_type == 'float' and expr_type == 'int'):
                self._error(f"Return type mismatch: expected {return_type}, got {expr_type}", node)
    
    def _check_assignment(self, target_type, value_node, context_node):
        """Check if assignment type is compatible"""
        value_type = self._get_expression_type(value_node)
        
        # Allow int to float conversion
        if target_type == 'float' and value_type == 'int':
            return True
        
        if target_type != value_type:
            self._error(f"Type mismatch: cannot assign {value_type} to {target_type}", context_node)
            return False
        
        return True
    
    def _get_expression_type(self, node):
        """Infer expression type"""
        if node.node_type == 'literal':
            if node.value in ['true', 'false']:
                return 'bool'
            elif '.' in node.value:
                return 'float'
            elif node.value.isdigit() or (node.value[0] == '-' and node.value[1:].isdigit()):
                return 'int'
            else:
                return 'string'
        elif node.node_type == 'identifier':
            if node.value in self.symbols:
                return self.symbols[node.value]['type']
            else:
                self._error(f"Undefined variable '{node.value}'", node)
                return 'int'  # Default fallback
        elif node.node_type == 'binary_expression':
            left_type = self._get_expression_type(node.children[0])
            right_type = self._get_expression_type(node.children[1])
            
            # Type promotion rules
            if 'string' in [left_type, right_type]:
                return 'string'
            elif 'float' in [left_type, right_type]:
                return 'float'
            elif 'int' in [left_type, right_type]:
                return 'int'
            else:
                return 'bool'
        
        return 'int'  # Default type
    
    def _error(self, message, node):
        self.errors.append(f"Line {node.line}: {message}")