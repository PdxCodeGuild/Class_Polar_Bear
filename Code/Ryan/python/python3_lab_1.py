score = input('Please enter a number representing the score (0-100): ')
# Need to do an input validation if a letter is typed in this will be taught in 102 and requires
# a 'try' / 'except' structure to see if using the float() function on the str would produce an error.
score = float(score)
specific_score = score % 10

'''
Long hand of the same as modulus
if score >= 90 and score < 94.5:
    grade = 'A-'
elif score >= 94.5 and score < 95.5:
    grade = 'A'
elif score >= 95.5 and score <= 100:
    grade = 'A+'
'''
if score == 100:
    grade = 'A'
    specific_score = 9
elif score >= 90 and score < 100:
    grade = 'A'
elif score >= 80 and score < 90:
    grade = 'B'
elif score >= 70 and score < 80:
    grade = 'C'
elif score >= 60 and score < 70:
    grade = 'D'
elif score >= 0 and score < 60:
    grade = 'F'
    specific_score = 5
    # There is no F+ or F- letter grade so setting the variable to a fixed number to complete the following if statement
else:
    print('Please enter a valid score 0-100')
#print(specific_score)
if specific_score < 4.5:
    specific_grade = '-'
elif specific_score >= 5.5:
    specific_grade = '+'
elif specific_score >= 4.5 and specific_score < 5.5:
    specific_grade = ' '
else:
    print('')
#print(type(score))
print(f'Your score of ({score}) is a(n) {grade}{specific_grade}')