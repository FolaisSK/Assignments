password = input("Enter Password: ")

password_length = len(password) 

if password_length > 6 and password_length <= 10:
	print("Medium")
elif password_length < 6:
	print("Weak")
elif password_length > 10:
	print("Strong")
elif password_length < 1:
	print("Invalid")
