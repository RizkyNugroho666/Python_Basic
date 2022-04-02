

users = open("users.txt", "r") # "r" itu read, "w" itu write,

print(users.read()) # Akan membaca file secara langsung

users.close()

# open(folder/subfolder/file.txt) ini adahal contoh jika file yang akan dibuka di folder yang berbeda

#===================================================================================

users = open("users.txt", "r") 

array = users.readline() # Akan membaca file secara satu baris

print(array)

users.close()
#===================================================================================

users = open("users.txt", "r") 

array = users.readlines() # Akan membaca seluruh file dalam satu baris menjadi list

print(array[2]) # jika diberi parameter 2, maka akan mencetak baris di elemen ke 2 (sama seperti list)

users.close()

#===================================================================================

users = open("users.txt", "r") 

array = users.readlines() # Akan membaca seluruh file dalam satu baris menjadi list

index = 1
for user in array: #setiap data yang ada di file akan dimunculkan secara loop
    print(f"{index} - {user}") #setiap baris akan ditambah urutan angka
    index +=1 #setiap perulangan index nya akan bertambah sesuai banyaknya baris yg dicetak

users.close()