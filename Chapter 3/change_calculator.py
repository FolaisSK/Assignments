# Prompt user to input price between 0 and 1
#If the price inputed is less greater Thant 1 or less than 0 print Invalid input
#Else calculate change
#Round up the change to whole number
#Calculate quarters (25), dimes (10), nickels(5), pennies
#Print Change if it is greater than 0
#qed. 



price = float(input("Enter purchase price (in dollars, <= 1): "))

if price > 1 or price < 0:
    print("Invalid price. Must be between 0 and 1.")
else:
    # Calculate change in cents
    change = round((1 - price) * 100)


    quarters = change // 25
    change %= 25

    dimes = change // 10
    change %= 10

    nickels = change // 5
    change %= 5

    pennies = change

    print("Your change is:")
    if quarters > 0:
        print(f"{quarters} quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")
