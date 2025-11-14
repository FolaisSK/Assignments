user_age = int(input("Enter your age: "))

max_heart_rate = 220 - user_age

min_heart_range = max_heart_rate * 0.5
max_heart_range = max_heart_rate * 0.85

print("Your Maximum heart rate is ", max_heart_rate, "bpm")
print("The Target Range for your heart rate is ", min_heart_range, " to ", max_heart_range, "bpm")


