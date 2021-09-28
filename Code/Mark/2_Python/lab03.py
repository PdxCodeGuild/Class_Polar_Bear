# convert numerical score to letter grade
score = int(input('Please input numerical score from 0 to 100: '))
if score < 0 or score > 100:
	print('Invalid score entered.')
else:
	grade = 'A'
	if score < 60:
		grade = 'F'
	elif score < 70:
		grade = 'D'
	elif score < 80:
		grade = 'C'
	elif score < 90:
		grade = 'B'
	print(f'A numerical score of {score} is equal to a grade of {grade}.')

