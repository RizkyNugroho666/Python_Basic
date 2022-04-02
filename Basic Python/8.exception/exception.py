# Exception (Menghandle error agar program tidak crash)

try: # Ini adalah exception error handling
    level = input("Masukan Level kamu: ") # Masukan dengan angka
    level = int(level) # Angka tidak bisa di convert ke Integer, maka akan error jika di convert
    print(level)

except ValueError: # Jika tipe error nya adalah ValueError maka program tidak akan crash
    print("Yang kamu masukan bukan angka!") # Ini yang akan muncul jika tipe error nya adalah "ValueError"