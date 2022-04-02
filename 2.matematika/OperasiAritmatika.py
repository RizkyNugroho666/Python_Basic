# belajar operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,'+',b, '=',hasil)


# operasi pengurangan -
hasil = a - b
print(a,'-',b, '=',hasil)


# operasi perkalian *
hasil = a * b
print(a,'*',b, '=',hasil)


# operasi pembagian /
hasil = a / b
print(a,'/',b, '=',hasil)


# operasi eksponen (pangkat) "**"
hasil = a ** b
print(a,'**',b, '=',hasil)


# operasi modulus % sisa pembagian
hasil = a % b
print(a,'%',b, '=',hasil)

# operasi floor division //
hasil = a // b
print(a,'//',b, '=',hasil)

# Prioritas operasi, operational presedence
## Akan dikerjakan yang lebih prioritas
### Misal kurang dan bagi, maka yang akan dikerjakan yaitu yg pembagian terlebih dahulu
'''
    1. ()
    2. eksponen **
    3. perkalian dan kawan-kawan * / ** % //
    4. pertambahan dan pengurangan

'''

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

# Kurung akan mengambil langkah paling pertama/prioritas
hasil = (x + y) * z
print('(',x,'+',y,') *',z,'=',hasil)
