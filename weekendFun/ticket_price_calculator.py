buyers_age = int(input("Enter your age: "))

if buyers_age < 5:
	print("Ticket is Free")
elif buyers_age >= 5 and buyers_age < 13:
	print("Ticket price is $5")
elif buyers_age >= 13 and buyers_age < 65:
	print("Ticket price is $12")
else:
	print("Ticket price is $8")