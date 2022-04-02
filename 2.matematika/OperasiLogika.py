# operasi logika atau boolean

# not, or, and, xor

# OR (Jika salah satu true, maka hasilnya akan true)
a = False
b = False
c = a or b
print(f"{a} OR {b} = {c}")

a = True
b = False
c = a or b
print(f"{a} OR {b} = {c}")

a = False
b = True
c = a or b
print(f"{a} OR {b} = {c}")

a = True
b = True
c = a or b
print(f"{a} OR {b} = {c}")

# AND =======================================
# Jika dua buah nilai true, maka hasilnya akan true
print(f"\n=======AND=======\n")

a = False
b = False
c = a and b
print(f"{a} and {b} = {c}")

a = True
b = False
c = a and b
print(f"{a} and {b} = {c}")

a = False
b = True
c = a and b
print(f"{a} and {b} = {c}")

a = True
b = True
c = a and b
print(f"{a} and {b} = {c}")

print(f"\n=======XOR=======\n")

# XOR ^ (akan true jika salah satu true, sisanya false)
a = False
b = False
c = a ^ b
print(f"{a} XOR {b} = {c}")

a = True
b = False
c = a ^ b
print(f"{a} XOR {b} = {c}")

a = False
b = True
c = a ^ b
print(f"{a} XOR {b} = {c}")

a = True
b = True
c = a ^ b
print(f"{a} XOR {b} = {c}")
