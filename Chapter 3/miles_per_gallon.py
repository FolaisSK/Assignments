#Initialise total miles and total gallons
#Create a loop for gallons used with a dummy value to break it
#Prompt the user to enter the miles driven
#Calculate miles per gallon
#display the mpg
#Keep adding the miles and gallons for each entry
#If the gallons is greater than zero, print overall mpg else print nothing was inputed





total_miles = 0.0
total_gallons = 0.0

while True:
    gallons = float(input("Enter the gallons used (-1 to end): "))
    if gallons == -1:
        break

    miles = float(input("Enter the miles driven: "))
    mpg = miles / gallons

    print(f"The miles/gallon for this tank was {mpg}")

    total_miles += miles
    total_gallons += gallons

if total_gallons > 0:

    overall_mpg = total_miles / total_gallons

    print(f"The overall average miles/gallon was {overall_mpg}")

else:

    print("Nothing to calculate.")
