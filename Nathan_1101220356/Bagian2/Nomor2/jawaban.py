'''
# EXAMPLES

# Input
Masukkan angka : 377
# Expected result
Angka 377 merupakan angka fibonnaci

# Input
Masukkan angka : 9
# Expected result
Angka 9 bukan angka fibonnaci
'''
import math

#cek apakah bentuk persegi


def isPerfectSquare(x):
	s = int(math.sqrt(x))
	return s*s == x

def isFibonacci(n):

	# n adalah Fibonacci jika 5*n*n + 4 atau 5*n*n - 4 atau keduanya
	# adalah persegi
	return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

a = int(input("Masukkan angka: "))
if (isFibonacci(a) == True):
	print("Angka " ,a, "merupakan angka fibonacci")
else:
	print("Angka",a, "bukan angka Fibonacci")

