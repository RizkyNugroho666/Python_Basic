# if 
x = 10
Genap = (x % 2 == 0)

if Genap:
    print("x adalah bilangan genap!")

# if/else
if Genap:
    print("x adalah bilangan genap!")

else:
    print("x bukan bilangan genap!")

# If/Elif/Else
# Ketentuan:
# - Elif bisa lebih dari 1
# - If dan Else masing-masing max 1 saja
x = -7

if x > 0:
    print("x adalah bilangan positif!")

elif x < 0:
    print("x adalah bilangan negatif")

else:
    print("x adalah nol!")