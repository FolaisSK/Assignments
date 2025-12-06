import math
pizza_type = input("Enter Pizza Type: ")
guests = int(input("Enter Number of Guests: "))

boxes_of_pizza = 0
slices_leftover = 0
price = 0

if guests >= 0:

	if pizza_type.lower() == "sapa size":

		number_of_slices = 4
		price_per_box = 2000

		boxes_of_pizza = math.ceil(guests / number_of_slices)
		slices_leftover = number_of_slices - guests % number_of_slices
		price = price_per_box * boxes_of_pizza

	elif pizza_type.lower() == "small money":

		number_of_slices = 6
		price_per_box = 2400

		boxes_of_pizza = math.ceil(guests / number_of_slices)
		slices_leftover = number_of_slices - guests % number_of_slices
		price = price_per_box * boxes_of_pizza

	elif pizza_type.lower() == "big boys":

		number_of_slices = 8
		price_per_box = 3000

		boxes_of_pizza = math.ceil(guests / number_of_slices)
		slices_leftover = number_of_slices - guests % number_of_slices
		price = price_per_box * boxes_of_pizza

	elif pizza_type.lower() == "odogwu":

		number_of_slices = 12
		price_per_box = 4200

		boxes_of_pizza = math.ceil(guests / number_of_slices)
		slices_leftover = number_of_slices - guests % number_of_slices
		price = price_per_box * boxes_of_pizza

	else:

		print("Invalid Pizza Type Oga")

else:
	print("Why are you putting negative number?")

print("Number of boxes of pizza to buy = ", boxes_of_pizza)
print("Number of left over slices after serving = ", slices_leftover)
print("Prices = ", price)