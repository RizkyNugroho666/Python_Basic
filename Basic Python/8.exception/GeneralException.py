# Exception (Menghandle error agar program tidak crash)

try: # Ini adalah exception error handling
    level = input("Masukan Level kamu: ") # Masukan dengan angka
    level = int(level) # Angka tidak bisa di convert ke Integer, maka akan error jika di convert
    print(level)

except: # Akan meng-handle segala tipe error, tanpa harus memasukan error secara spesifik
    print("Terjadi kesalahan!")