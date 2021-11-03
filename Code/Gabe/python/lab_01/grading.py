grade = input('Enter number grade: ')

try:
  grade = float(grade)
except ValueError:
  print('Please enter a number from 0 to 100.')

if grade <= 100 and grade >= 90:
  if grade <= 100 and grade > 95:
    print('A+')
  elif grade == 95:
    print('A')
  elif grade >= 90 and grade < 95:
    print('A-')
elif grade < 90 and grade >= 80:
  if grade < 90 and grade > 85:
    print('B+')
  elif grade == 85:
    print('B')
  elif grade >= 80 and grade < 85:
    print('B-')
elif grade < 80 and grade >= 70:
  if grade < 80 and grade > 75:
    print('C+')
  elif grade == 75:
    print('C')
  elif grade >= 70 and grade < 75:
    print('C-')
elif grade < 70 and grade >= 60:
  if grade < 70 and grade > 65:
    print('D+')
  elif grade == 65:
    print('D')
  elif grade >= 60 and grade < 65:
    print('D-')
elif grade < 60 and grade >= 0:
  print('F')
else:
  print('Please enter a valid number between 0 and 100.')