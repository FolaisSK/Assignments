first_number = float(input("Enter a number: "))
second_number = float(input("Enter a number: "))

operator = input("Enter an operator (+, -, *, /): ")

sum = first_number + second_number
difference = first_number - second_number
product = first_number * second_number
division = first_number / second_number

if operator == '+':
	print("Sum: ", sum)
elif operator == '-':
	print("Difference: ", difference)
elif operator == '*':
	print("Product: ", product)
elif operator == '/':
	print("Division: ", division)
else:
	print("Oops, Invalid.")



