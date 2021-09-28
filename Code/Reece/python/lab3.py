# Reece Adams - lab3.py - Grading #
import math

max_grade = 100
grade = input("Enter your grade: ")

try:
    grade = (int(grade))
except ValueError:
    print("That was not a number...")
    exit()

# Math for letter_grade --------------------------- #

if grade > 100:
    print("Grade entered too high...")
    exit()
elif grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60:
    letter_grade = 'D'
elif grade >= 0:
    letter_grade = 'F'
else:
    print("Grade entered too low...")
    exit()

modu_perc = max_grade % grade

if modu_perc <= 3:
    symbol = '+'
elif modu_perc <= 6:
    symbol = ''
else:
    symbol = '-'


print(f'Your grade {grade} results in a {letter_grade}{symbol}')