number_one = int(input("Enter an integer (a): "))
number_two = int(input("Enter an integer (b): "))
number_three = int(input("Enter an integer (c): "))

largest = number_one

if number_two > number_one and number_two > number_three:
	largest = number_two
	

if number_three > number_two and number_three > number_one:
	largest = number_three


print("The Largest number is:", largest)




