def prime_equals_palindrome(number):
	count_factor = 0
	for count in range(1, number, 1):
		if number % count == 0:
			count_factor += 1

#	if count_factor == 2:
#		prime_number = 'sharp'

	reverse = 0
	initial_number = number
	while number != 0:
		digit = number % 10
		reverse = reverse * 10 + digit
		number /= 10

#	if initial_number == reverse:
#		palindrome = 'sharp'

	if count_factor == 2 and initial_number == reverse:
		return True
	else:
		return False


print(prime_equals_palindrome(131))



	
	