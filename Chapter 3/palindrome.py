#Prompt the user to enter a five digit integer
#While the number is in the range of five digits continue
#Declare a divisor variable
#Pick out the digits one by one
#If the first digit is equal to the fifth digit and the second digit is equal to the fourth digit print it is a palindrome
#Else print it is not a palindrome


number = int(input("Enter a five-digit integer: "))

while number < 10000 or number > 99999:
    number = int(input("Invalid. Enter a five-digit integer: "))

divisor = 10000

digit_one = number // divisor 
print(digit_one, end="  ")
number_two = number % divisor 
divisor //= 10 

digit_two = number_two // divisor
print(digit_two, end="  ")
number_three = number_two % divisor
divisor //= 10

digit_three = number_three // divisor
print(digit_three, end="  ")
number_four = number_three % divisor
divisor //= 10

digit_four = number_four // divisor
print(digit_four, end="  ")
number_five = number_four % divisor
divisor //= 10

digit_five = number_five // divisor
print(digit_five)


if digit_one == digit_five and digit_two == digit_four:
	print(number, " is a PALINDROME")
else:
	print(number, " is NOT a palindrome")