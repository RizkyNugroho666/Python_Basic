# CASTING DATA = merubah dari satu tipe ke tipe lain
# data integer
print("========INTEGER=========")
data_int = 9;
print("data = ", data_int, ", type = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai integer = 0
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))

# data float
print("========FLOAT=========")
data_float = 10.5;
print("data = ", data_float, ", type = ", type(data_float))

data_int = int(data_float) #akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) #akan false jika nilai float = 0
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))

# data boolean (kali ini menggunakan rumus print yang lebih simple)
print("========BOOLEAN=========")
data_bool = False;
print(f"data = {data_bool}", "type = ", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print(f"data = {data_int}", "type = ", type(data_int))
print(f"data = {data_str}", "type = ", type(data_str))
print(f"data = {data_float}", "type = ", type(data_float))

# data string
print("========STRING=========")
data_str = "10" #jika menggunakan angka maka dapat diubah menjadi data integer
print(f"data = {data_str}", "type = ", type(data_str))

data_int = int(data_str) #data str ("Si Ucup") dengan huruf/kosong tidak akan bisa dirubah menjadi data integer
data_float = float(data_str) #string harus angka
data_bool = bool(data_str) #akan false jika nilai string = 0
print(f"data = {data_int}", "type = ", type(data_int))
print(f"data = {data_float}", "type = ", type(data_float)) 
print(f"data = {data_bool}", "type = ", type(data_bool))

# data complex
print("========COMPLEX=========")
data_complex = 5,5 #Data complex yang berupa bilangan koma "," tidak bisa diubah ke data int/float/str
print(f"data complex = {data_complex}", "type = ", type(data_complex)) #data complex berarti angka yang memiliki koma "," atau tuple

#data_int = int(data_complex) # data int adalah bilangan angka yang tidak memiliki koma ",/."
#data_float = float(data_complex) # data float adalah bilangan angka yang memiliki koma dari titik "."
data_str = str(data_complex)
#print(f"data = {data_int}", "type = ", type(data_int))
#print(f"data = {data_float}", "type = ", type(data_float))
print(f"data = {data_str}", "type = ", type(data_str))