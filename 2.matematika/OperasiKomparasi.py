# Operasi Komparasi

# setiap hasil dari operasi komparasi adalah boolean (hanya ada true/false)

# >,<,>=,<=,==,!=,is,is not

# diketahui:
a = 5
b = 3
 
print(f"\n=====LEBIH DARI=====")
 # > lebih dari
hasil = a > 3
print(f"a > 3 = {hasil}") #hasil nya akan true karena 5 lebih banyak dari 3 (false jika sebaliknya)
hasil = b > 6
print(f"b > 6 = {hasil}") 

print(f"\n=====KURANG DARI=====")
# < kurang dari
hasil = b < a
print(f"b < a = {hasil}")#hasil nya akan true karena b(3) lebih sedikit dari a(5) (false jika sebaliknya)
hasil = a < b
print(f"a < b = {hasil}")

print(f"\n=====LEBIH DARI SAMA DENGAN=====")
# >= lebih dari sama dengan
hasil = a >= 5
print(f"a >= 5 = {hasil}") # jika angkanya sama maka akan tetap true
hasil = a >= 10
print(f"a >= b = {hasil}")

print(f"\n=====KURANG DARI SAMA DENGAN=====")
# <= kurang dari sama dengan
hasil = b <= 3
print(f"b <= 3 = {hasil}") 
hasil = a <= 4
print(f"b <= 3 = {hasil}") 

print(f"\n=====SAMA DENGAN=====")
# == sama dengan
hasil = a == 5 # akan di cek apakah a sama dengan 5, jika sama akan true, jika berbeda akan false
print(f"a == 5 = {hasil}")
hasil = a == 4
print(f"a == 4 = {hasil}")

print(f"\n=====TIDAK SAMA DENGAN=====")
# != tidak sama dengan
hasil = a != 5 # jika sama akan menjadi false, jika tidak sama akan true
print(f"a != 5 = {hasil}")
hasil = b != a
print(f"b != a = {hasil}")

print(f"\n=====is=====\n")
# 'is' sebagai komparasi object identity
x = 5 # ini adalah assignment membuat object
y = 5
z = 10
print(f"nilai x = {x} id = {hex(id(x))}")
print(f"nilai y = {y} id = {hex(id(y))}")
print(f"nilai z = {z} id = {hex(id(z))}")
hasil = x is y # wajib menggunakan variabel(a is b), bukan literal "x is 10"(itu salah)
print(f"x is y = {hasil}")
hasil = x is z
print(f"x is z = {hasil}")

print(f"\n=====is not=====\n") #is not adalah kebalikan dari 'is' sama seperti (== dan !=)
# 'is not' sebagai komparasi object identity
x = 5 # ini adalah assignment membuat object
y = 5
z = 10
print(f"nilai x = {x} id = {hex(id(x))}")
print(f"nilai y = {y} id = {hex(id(y))}")
print(f"nilai z = {z} id = {hex(id(z))}")
hasil = x is not y # wajib menggunakan variabel(a is b), bukan literal "x is 10"(itu salah)
print(f"x is y = {hasil}")
hasil = x is not z
print(f"x is z = {hasil}")