# belajar function dengan parameter

def halo_user(name, level): #yang ada di dalam kurung adalah parameter
    print(f"halo {name} - {level}") # {name} dan {level} di dapat dari parameter di atas
    print("Selamat pagi!")

halo_user("Rizky", 8) # "Rizky" dan "angka" adalah parameter (name) dan (level) dari function
halo_user(level= "10", name= "rizky") # dapat di balik parameter nya tetapi hasilnya akan tetap sama/urut meskipun di balik
print("=========")
halo_user("Zelda", 10) # dapat memanggil function berkali - kali dengan nama parameter yang berbeda


length = len([1, 2, 3])
print(length)











