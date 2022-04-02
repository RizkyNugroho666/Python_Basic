numbers = (1, 2, 3)

x, y, z, = numbers

print(z)

numbers = (1, 2, 3) #angka index

x, *y = numbers #karena hanya ada 2 variable, maka tanda "*" berarti akan memasukan angka index sisanya kedalam variable y

print("")
print(x)
print(y)