total_bill = float(input("Enter total bill: "))
is_member = input("Are you a member, yes or no?")

if total_bill >= 1000 and is_member == "yes":
	discount = total_bill * 0.10
	new_bill = total_bill - discount
	print("You have a 10% discount, new bill is ", new_bill)
elif total_bill >= 1000 and is_member != "yes":
	discount = total_bill * 0.05
	new_bill = total_bill - discount
	print("You have a 5% discount, new bill is ", new_bill)
else:
	print("You have no discount, your bill is ", total_bill)


	