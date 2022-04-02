# operator bitwise, operasi biner, binary

a = 9
b = 5

# bitwise OR (|)
c = a | b
print('\n======OR======')
print(f"Nilai : {a} binary : {format(a,'08b')}")
print(f"Nilai : {b} binary : {format(b,'08b')}")
print('------------------------- (|)')
print(f"Nilai : {c} binary : {format(c,'08b')}")

# bitwise AND (&)
c = a & b
print('\n======AND======')
print(f"Nilai : {a} binary : {format(a,'08b')}")
print(f"Nilai : {b} binary : {format(b,'08b')}")
print('------------------------- (&)')
print(f"Nilai : {c} binary : {format(c,'08b')}")

# bitwise XOR (^)
c = a ^ b
print('\n======XOR======')
print(f"Nilai : {a} binary : {format(a,'08b')}")
print(f"Nilai : {b} binary : {format(b,'08b')}")
print('------------------------- (^)')
print(f"Nilai : {c} binary : {format(c,'08b')}")

# bitwise NOT (~)
c = ~a
print('\n======NOT======')
print(f"Nilai : {a} binary : {format(a,'08b')}")
print('------------------------- (~)')
print(f"Nilai : {c} binary : {format(c,'08b')}")
print('-------------------------(^)')
d = 0b0000001001
e = 0b1111111111
print(f"Nilai : {e^d} binary : {format(e^d,'08b')}")


# shifting

# shifting right (>>)
c = a >> 1
print('\n======>>======')
print(f"Nilai : {a} binary : {format(a,'08b')}")
print('------------------------- (>>)')
print(f"Nilai : {c} binary : {format(c,'08b')}")

# shifting left (<<)
c = a << 1
print('\n======<<======')
print(f"Nilai : {a} binary : {format(a,'08b')}")
print('------------------------- (<<)')
print(f"Nilai : {c} binary : {format(c,'08b')}")




