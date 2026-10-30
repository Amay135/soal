import math

pilihan = int(input("Pilihan (1 = keliling, 2 = luas): "))
r = float(input("Masukkan jari-jari : "))

if pilihan == 1:
    print("Keliling lingkaran:", 2 * math.pi * r)
elif pilihan == 2:
    print("Luas lingkaran:", math.pi * r ** 2)
else:
    print("Pilihan tidak valid")