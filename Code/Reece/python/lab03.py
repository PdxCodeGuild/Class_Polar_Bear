# Reece Adams - lab03.py - lab 3 - Grading #

import math

grade = input("Enter your grade: ")

try:
    grade = (float(grade))
    if grade > 100 or grade < 0:
        raise ValueError
except ValueError:
    print("Inavlid grade... goodbye.")
    exit()

# Math for letter_grade --------------------------- #

if grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Math for symbol ---------------------------- #

ones_digit = grade % 10

# print(ones_digit)

if grade >= 60:
    if ones_digit >= 7 or grade == 100:
        letter_grade += '+'
    elif ones_digit <= 3:
        letter_grade += '-'

print(f'Your grade {grade} results in a(n) {letter_grade}')