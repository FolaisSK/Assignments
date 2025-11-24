sum = 0

for number in range(1, 20001):
	if number % 10 == 0:
		sum += number

print("The sum of numbers between 1 and 20000 is ", sum)