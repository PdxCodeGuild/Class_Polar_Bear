import grade

userGrade = input('What was your grade?')

try:
    userGrade = int(userGrade)
except ValueError:
    print('Please enter a number')
    exit()

print(grade.numberGrade(userGrade))