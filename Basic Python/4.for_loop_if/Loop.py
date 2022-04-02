# Loop = Perulangan
# - For

# Range 1 parameter
for lap in range(3):
    print("Ini loop")
    print("Ini juga loop")

print("ini bukan loop")

# Range 2 parameter: range(min, max)
# min - termasuk dirinya
# max - tidak termasuk dirinya
for lap in range(1,11):
    print(f"Loading... {lap}%")

# Range 3 parameter: range(awal, akhir, lompatan)
# awal - termasuk dirinya
# akhir - tidak termasuk dirinya
for lap in range(100, 0, -2):
    print(f"HP: {lap}")

print("You are dead")

#-------------------------------------------------------
# While

lap = 3
while lap > 0: #Selama lap lebih dari 0
    print("Looping")
    lap = lap - 1 #bisa pakai (lap -= 1)
    
print("Sudah tidak loop")
