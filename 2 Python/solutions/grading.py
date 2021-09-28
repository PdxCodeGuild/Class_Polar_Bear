

# Get the users number grade
number_grade = input("Enter your grade: ")

# Make sure its an integer
try:
    number_grade = float(number_grade)
    if number_grade > 100 or number_grade < 0:
        raise ValueError
except ValueError:
    print("Invalid grade... goodbye")
    exit()

letter_grade = None
ones_digit = number_grade % 10
if ones_digit == 9:
    number_grade = round(number_grade)
# Get the users letter grade
if number_grade >= 90 and number_grade <= 100:
    letter_grade = 'A'
elif number_grade >= 80:
    letter_grade = 'B'
elif number_grade >= 70:
    letter_grade = 'C'
elif number_grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'


# Get +/-
if number_grade >= 60:
    # 7 or greater is +
    if ones_digit >= 7 or number_grade == 100:
        letter_grade += "+"
    # 3 or below is -
    elif ones_digit <= 3:
        letter_grade += '-'

# Show the user their grade
print(f'Your grade {number_grade} results in a(n) {letter_grade}')