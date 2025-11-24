student_scores = 15
pass_count = 0

for scores in range (1, student_scores + 1):
	scores = int(input("Enter student scores:"))
	if scores > 45:
		pass_count += 1

print("The number of students that passed is ", pass_count)
	