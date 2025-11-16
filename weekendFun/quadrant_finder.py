number_one = int(input("Enter an integer (x): "))
number_two = int(input("Enter an integer (y): "))

if number_one > 0 and number_two > 0:
	print("Q1")

if number_one < 0 and number_two > 0:
	print("Q2")

if number_one < 0 and number_two < 0:
	print("Q3")

if number_one > 0 and number_two < 0:
	print("Q4")

if number_one == 0 and number_two == 0:
	print("Origin")

if number_one != 0 and number_two == 0:
	print("X-axis")

if number_one == 0 and number_two != 0:
	print("Y-axis")

