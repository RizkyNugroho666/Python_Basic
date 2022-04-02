import random

users = ['Rizky', 'Ageng', 'Nugroho']

batas_atas = 0
batas_bawah = len(users) - 1

random_int = random.randint(batas_atas, batas_bawah)

winner = users[random_int]
print(winner)