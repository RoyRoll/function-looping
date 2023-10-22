# Nama: Rio Ferddinansya
# NIM: J0403231004
# email: rioferddinansya@gmail.com
# konversi suhu

satuan=input("Pilih satuan suhu (C/F): ")
suhu=float(input("Masukan nilai suhu: "))

if satuan == "C":
    suhu=round((9 * suhu) / 5 + 32, 1)
    print("Suhu tersebut dalam Fahrenheit adalah:", suhu,"°F")
elif satuan == "F":
    suhu=round((suhu - 32) * 5 / 9, 1)
    print("Suhu tersebut dalam Celcius adalah:", suhu,"°C")
else:
    print("Invalid")
    