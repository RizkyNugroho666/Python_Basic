import Matematika # digunakan untuk import seluruh function

result = Matematika.plus(10, 8) #Nama module dan function harus ditulis, Matematika(Module), plus(function)
print(result)

result = Matematika.minus(10, 10)
print(result)


from Matematika import plus # digunakan untuk import 1 function. misalkan fuction "plus"

result = plus(10, 10)
print(result)