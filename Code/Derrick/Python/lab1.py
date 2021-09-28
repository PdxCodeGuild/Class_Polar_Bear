# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F

# 0-3: -
# 4-6: 
# 7-9: +

userGrade = input('What was your grade?')

try:
    userGrade = int(userGrade)
except ValueError:
    print('Please enter a number')
    exit()

def numberGrade(grade):
    letter = ''
    symbol = ''
    gradeStr = len(str(grade))
    lastDigit = str(grade)[-1]

    if grade >= 90:
        letter = 'A'
    elif grade >= 80:
        letter = 'B'
    elif grade >= 70:
        letter = 'C'
    elif grade >= 60:
        letter = 'D'

    if gradeStr == 3:
        return 'You got a 100!!!'
    elif grade <= 59:
        return 'You failed :('
    elif gradeStr == 2:
        if lastDigit >= '0' and lastDigit <= '3':
            symbol = '-'  
        elif lastDigit >= '4' and lastDigit <= '6':
            symbol = ''
        elif lastDigit <= '7' and lastDigit <= '9':
            symbol = '+'
    
    return letter + symbol

print(numberGrade(userGrade))




# if userGrade >= 90:
#     if userGrade <= 93:
#         print('You got an A-')
#     elif userGrade <= 96:
#        print('You got an A') 
#     elif userGrade <= 100:
#        print('You got an A+!!!!!')
# elif userGrade >= 80:
#     if userGrade <= 83:
#         print('You got a B-')
#     elif userGrade <= 86:
#        print('You got a B') 
#     elif userGrade <= 89:
#        print('You got a B+')
# elif userGrade >= 70:
#     if userGrade <= 73:
#         print('You got a C-')
#     elif userGrade <= 76:
#        print('You got a C') 
#     elif userGrade <= 79:
#        print('You got a C+')
# elif userGrade >= 60:
#     if userGrade <= 63:
#         print('You got a D-')
#     elif userGrade <= 66:
#        print('You got a D') 
#     elif userGrade <= 69:
#        print('You got a D+')
# else:
#     print('You failed')
