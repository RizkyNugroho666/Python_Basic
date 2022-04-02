# a = 10, a adalah variabel dengan nilai 10 
import time
start_time = time.time()
# tipe data: Angka satuan "integer"
data_integer = 1 #angka ini boleh puluhan atau jutaan (tidak ada koma)
print("data: ", data_integer)
print("- bertipe: ", type(data_integer))

# tipe data: Float adalah angka dengan koma
data_float = 1.5 #angka data float adalah angka yang terdiri dari koma (koma menggunakan titik ".")
print("data: ", data_float)
print("- bertipe: ", type(data_float))

# tipe data: "String" adalah kumpulan karakter/huruf
data_string = "SiUcup"
print("data: ", data_string)
print("- bertipe: ", type(data_string))

#tipe data: "Biner" adalah true/false (boolean)
data_bool = True #bisa True atau False
print("data ", data_bool)
print("- bertipe: ", type(data_bool))

# tipe data: Khusus
## Bilangan kompleks/complex
data_complex = complex(5,6) #pakai koma ","
print("data ", data_complex)
print("- bertipe: ", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double #bisa import data dari bahasa C misal c_char, c_double, c_buffer dll
data_c_double = c_double(10.5)
print("data ", data_c_double)
print("- bertipe: ", type(data_c_double))

print(time.time() - start_time, "detik")