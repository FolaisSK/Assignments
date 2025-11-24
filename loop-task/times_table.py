user_input = int(input("Enter a number: "))
count = 0

for count in range(1, 11):
	answer = user_input * count
	print(user_input, "x", count, "=", answer)