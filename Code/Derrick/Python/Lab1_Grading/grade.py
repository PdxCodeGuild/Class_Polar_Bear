# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F

# 0-3: -
# 4-6: 
# 7-9: +

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
        elif lastDigit >= '7' and lastDigit <= '9':
            symbol = '+'
    
    return letter + symbol