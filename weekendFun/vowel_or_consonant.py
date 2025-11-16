letter = input("Input any letter: ").lower()


if letter in ("a", "e", "i", "o", "u"):
	print("Vowel")
elif letter.isdigit():
	print("Invalid input")
else: 
	print("Consonant")




