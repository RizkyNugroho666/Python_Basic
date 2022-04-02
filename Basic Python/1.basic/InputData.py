# Belajar Input Data dari User

# data yang dimasukan pasti string
data = input("Masukan Username:")

print("Username = ", data,",type =", type(data))

# jika kita ingin mengambil int, maka
data_float = float(input("Masukan angka float: "))
data_int = int(input("Masukan angka integer: "))

print("data = ",data_int,",type = ", type(data_int))

# data boolean,kita coba menggunakan rumus print yang simple
biner = bool(int(input("Masukan data biner: ")))

print(f"biner= {biner} {type(biner)}") #ini menggunakan rumus print yang lebih simple