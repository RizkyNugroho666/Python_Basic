import csv

users = open("users.csv", "r")

users_csv = csv.reader(users, delimiter=",")

for row in users.csv:
    print(f"Name: {row[0]}. Username: {row[1]}. Role{row[-1]}")

users.close()