
x = 21
y = (x % 2 == 0)

if y:
    print("ini adalah bilangan genap!")

else:
    print("ini bukan bilangan ganjil!")


username_correct = "ucup"
password_correct = "ucup123"

username = input("Masukan username: ")
password = input("Masukan password: ")

login_success = (username_correct and password == password_correct)

if login_success:
    print("Login berhasil")
