#Initialise all the variables and declare deposit amount
#Print out the table header
#initialise a counter
#While counter is less than number of yrs calculate and print out the deposit amount that year
#Continue for 30 iterations


principal = 1000
rate = 7
return_rate = 0.07
years = 30
deposit_amount = 0

print("Years \t Rate \t Investment Return \t")
counter = 1

while counter <= years:
	deposit_amount += principal * ((1 + return_rate) ** counter)
	print(f"{counter} \t {rate} \t {deposit_amount:.2f} \t")
	counter += 1