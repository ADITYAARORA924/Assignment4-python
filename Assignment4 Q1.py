marks = float(input("Enter your marks: "))

if marks < 25:
    grade = "F"
elif marks < 45:
    grade = "E"
elif marks < 50:
    grade = "D"
elif marks < 60:
    grade = "C"
elif marks < 80:
    grade = "B"
else:
    grade = "A"

print("Your grade is:",grade)