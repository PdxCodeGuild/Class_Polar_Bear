# Take a user input number score and convert to a letter grade

#array of letter grades
letterGrade = ("A","B","C","D","F")

# input with error handling 
try:
    number_grade = float(input("Enter a score to get a letter grade: "))
    if number_grade < 0:
        raise ValueError
    if number_grade > 100:
        raise ValueError    
except ValueError:
    exit(print (" You did not enter a valid number"))
    
#store the letter grade in an empty string
grade = ''

#store the input in x and enumerate the array to check for the given condition
# then assign the index to the variable grade
for x in enumerate(letterGrade):
    x = number_grade
    if x >= 90:
        grade = letterGrade[0]            
        break
    if x >= 80:
        grade = letterGrade[1]
        break
    if x >= 70:
        grade = letterGrade[2]
        break
    if x >= 60:
        grade = letterGrade[3]
        break
    else:
        grade = letterGrade[4]
        break    
    #find the value of the inputs one position by using modulus operator
    # and given the condition add the string of + or - to the grade variable 
if number_grade % 10 > 7:
    print(grade + '+')
elif number_grade % 10 < 7:
    print(grade + '-')

            
