# latihan konversi satuan temperature

# program konversi celcius ke satuan lain
#=============================================

# celcius

print(f"\nPROGRAM KONVERSI TEMPERATUR\n")
celcius = float(input('Masukan suhu dalam celcius : ')) #suhu yang akan dikonversi ke temperatur lain
print(f"celcius adalah : {celcius} Celcius")

# reamur (4/5)C
reamur = (4/5) * celcius
print(f"celcius dalam reamur adalah: {reamur} reamur")

# fahrenheit (9/5)C
fahrenheit = ((9/5) * celcius) +32
print(f"celcius dalam fahrenheit adalah: {fahrenheit} fahrenheit")

# kelvin
kelvin = celcius + 273
print(f"celcius dalam kelvin adalah: {kelvin} kelvin")