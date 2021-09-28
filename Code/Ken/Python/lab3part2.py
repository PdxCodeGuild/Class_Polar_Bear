# Grading Lab

numerical_grade=input("What is your numerical grade for this Assignment?: ")


numerical_grade=float(numerical_grade)

if numerical_grade == 100:
    print("Your letter grade is A+")

elif numerical_grade >= 94 and numerical_grade <= 99:
    print("Your letter grade is A")

elif numerical_grade >= 90 and numerical_grade <= 93:
    print("Your letter grade is A-")

elif numerical_grade >= 87 and numerical_grade <= 89:
    print("Your letter grade is B+")

elif numerical_grade >= 83 and numerical_grade <= 86:
    print("Your letter grade is B")

elif numerical_grade >= 80 and numerical_grade <= 82:
    print("Your letter grade is B-")

elif numerical_grade >= 77 and numerical_grade <= 79:
    print("Your letter grade is C+")

elif numerical_grade >= 73 and numerical_grade <= 76:
    print("Your letter grade is C")

elif numerical_grade >= 70 and numerical_grade <= 72:
    print("Your letter grade is C-")

elif numerical_grade >= 67 and numerical_grade <= 69:
    print("Your letter grade is D+")

elif numerical_grade >= 63 and numerical_grade <= 66:
    print("Your letter grade is D")

elif numerical_grade >= 60 and numerical_grade <= 62:
    print("Your letter grade is D-")

else:
    print("Your letter grade is F")