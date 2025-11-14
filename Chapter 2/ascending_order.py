first_number = int(input("Enter a number: "))
second_number = int(input("Enter a number: "))
third_number = int(input("Enter a number: "))

if first_number >= second_number and first_number >= third_number:
	if second_number >= third_number:
		print(first_number, second_number, third_number)
	else:
		print(first_number, third_number, second_number)
elif second_number >= first_number and second_number >= third_number:
	if first_number >= third_number:
		print(second_number, first_number, third_number)
	else:
		print(second_number, third_number, first_number)
elif third_number >= first_number and third_number >= second_number:
	if first_number >= second_number:
		print(third_number, first_number, second_number)
	else:
		print(third_number, second_number, first_number)



