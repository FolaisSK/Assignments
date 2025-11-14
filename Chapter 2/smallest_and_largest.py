first_integer = int(input("Enter an integer: "))
second_integer = int(input("Enter an integer: "))
third_integer = int(input("Enter an integer: "))

sum = first_integer + second_integer + third_integer

average = sum / 3

product = first_integer * second_integer * third_integer


print("The Sum of the integers is ", sum)
print("The Average of the integers is ", average)
print("The Product of the integers is ", product)


if first_integer > second_integer and first_integer > third_integer:
	print("The Largest number is ", first_integer)
elif second_integer > first_integer and second_integer > third_integer:
	print("The Largest number is ", second_integer)
elif third_integer > first_integer and third_integer > second_integer:
	print("The Largest number is ", third_integer)
else:
	print("Some or all numbers are equal")


if first_integer < second_integer and first_integer < third_integer:
	print("The Smallest number is ", first_integer)
elif second_integer < first_integer and second_integer < third_integer:
	print("The Smallest number is ", second_integer)
elif third_integer < first_integer and third_integer < second_integer:
	print("The Smallest number is ", third_integer)
else:
	print("Some or all numbers are equal")


