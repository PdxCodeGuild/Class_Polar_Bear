# Grading Lab

numerical_grade=input("What is your numerical grade for this Assignment?: ")


numerical_grade=float(numerical_grade)


if numerical_grade >= 90:
    print("Your letter grade is A")

elif numerical_grade >= 80 and numerical_grade <= 89:
    print("Your letter grade is B")

elif numerical_grade >= 70 and numerical_grade <= 79:
    print("Your letter grade is C")

elif numerical_grade >= 60 and numerical_grade <= 69:
    print("Your letter grade is D")

else:
    print("Your letter grade is F")