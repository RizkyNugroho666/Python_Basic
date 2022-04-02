numbers = [5, 6, 7, 8, 1]
#menjumlahkan dengan rumus init
init_number = 0
for number in numbers:
    init_number = init_number +number

print(init_number)

#menjumlahkan dengan rumus sum
numbers = [5, 6, 7, 8, 1]
total = sum(numbers)
print(total)

#mencari angka maksimal
numbers = [5, 6, 7, 8, 1]
max_number = max(numbers)
print(max_number)

#mengurutkan bilangan dari kanan (menggunakan -)
numbers = [5, 6, 7, 8, 1]
numbers.sort()
max_number = numbers[-1] #Jika mines maka akan diurutkan dari kanan
print(max_number)

numbers = [5, 6, 7, 8, 1]
max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)