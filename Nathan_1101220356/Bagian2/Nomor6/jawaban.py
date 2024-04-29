'''
# EXAMPLES

# Input
Masukkan kata pertama : alur
Masukkan kata kedua   : ular
# Expected result
alur dan ular adalah anagram

# Input
Masukkan kata pertama : alur
Masukkan kata kedua   : liar
# Expected result
alur dan liar bukan anagram
'''

# function to check if two strings are
# anagram or not 
def check(s1, s2):
	
	# the sorted strings are checked 
	if(sorted(s1)== sorted(s2)):
		print(s1, "dan", s2, "adalah anagram.") 
	else:
		print(s1, "dan", s2, "bukan anagram.") 	 
		
# driver code 
s1 = str(input("Masukkan kata pertama: "))
s2 = str(input("Masukkan kata kedua: "))
check(s1, s2)
