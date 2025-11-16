user_weight = float(input("Enter weight in (kg): "))
user_height = float(input("Enter height in (meters): "))

body_mass_index = user_weight / (user_height * user_height)

if body_mass_index < 18.5:
	print("This user is Underweight")
elif body_mass_index >= 18.5 and body_mass_index < 25:
	print("This user in Normal")
elif body_mass_index >= 25 and body_mass_index < 30:
	print("This user is Overweight")
else:
	print("This user is OBESE!!") 

 