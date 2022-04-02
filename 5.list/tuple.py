
numbers = [5, 3, 1, 2, 4] # jika diubah ke tuple "()" maka akan error
print(numbers) # karena tuple tidak dapat diubah "immutable"
numbers[0] = 10
print(numbers)

numbers = [5, 3, 1, 2, 4]
print(numbers[2])