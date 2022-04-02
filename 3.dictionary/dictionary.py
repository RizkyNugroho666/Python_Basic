user = {
    "name": "Rizky Nugroho",
    "age": 18,
    "is_admin": True
}

name = user["name"] # akan mencetak nama dari data variable user
print("")
print(name)

#----------------------------
user = {
    "name": "1ntrovert skrrt",
    "age": "18",
    "is_admin": False
}

name = user.get("username", "1ntrovertskrrt") #jika key username tidak ada, maka akan mencetak "1ntrovertskrrt"
print("")
print(name)

#----------------------------
user = {
    "name": "Rizky Ageng Nugroho",
    "age": "18",
    "is_admin": True
}

user["username"] = "Rizky_Ageng_Nugroho" # jika memasukan keyword "username" maka akan mencetak "Rizky_Ageng_Nugroho"
user["name"] = "Rizky AN." # jika memasukan keyword "name", maka yang akan dicetak adalah nama "Rizky AN"

name = user.get("name")

print("")
print(name)