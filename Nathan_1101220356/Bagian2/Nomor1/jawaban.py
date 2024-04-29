'''
# EXAMPLES

# Input
Masukkan angka : 68
# Expected result
Angka 68 adalah bilangan genap

# Input
Masukkan angka : 21
# Expected result
Angka 21 adalah bilangan ganjil
'''

angka = int(input("Masukkan Angka: "))

if angka%2 == 0:
    print("Angka ", angka, "adalah bilangan genap")

else:
    print("Angka ", angka, "adalah bilangan ganjil")