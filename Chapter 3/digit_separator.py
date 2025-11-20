#Prompt the user for a five digit number
#Create a while loop to keep asking for a five digit integer then keep running if the number is a five digit integer
#Initialise the divisor to be 10000
#Create a while loop to divide the number by the divisor to get the left digit
#display the digit gotten with a space after
#Use modulo to remove the digit
#Use floor division to reduce the divisor then it moves to the next digit




number = int(input("Enter a five-digit integer: "))

while number < 10000 or number > 99999:
    number = int(input("Invalid. Enter a five-digit integer: "))

divisor = 10000

while divisor > 0:
    digit = number // divisor 
    print(digit, end="  ")
    number = number % divisor 
    divisor //= 10 
