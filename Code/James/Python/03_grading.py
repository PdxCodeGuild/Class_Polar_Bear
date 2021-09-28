'''
*'-.-'*'-.-'*'-.-'*'--'*
    Project: Full Stack Evening Boot Camp - Python Lab (03 Grading)
      Version: 1.0
Author: James Thornton
  Email: James.ed.thornton@gmail.com
      Date: 27 SEP 2021
*'-.-'*'-.-'*'-.-'*'--'*
'''


'''part 1


score = input('Input your grade as a number: ')

score = int(score)

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(grade)'''


# Part 2 


score = input('Input your grade as a number: ')

score = float(score)

if score >= 90:
    grade = "A"
    if score >=97.33:
        sign = "+"
    if score >=93.66:
        sign = ""
    if score >=90:
        sign = "-"
elif score >= 80:
    grade = "B"
    if score >=87.33:
        sign = "+"
    if score >=83.66:
        sign = ""
    if score >=80:
        sign = "-"
elif score >= 70:
    grade = "C"
    if score >=77.33:
        sign = "+"
    if score >=73.66:
        sign = ""
    if score >=70:
        sign = "-"
elif score >= 60:
    grade = "D"
    if score >=67.33:
        sign = "+"
    if score >=63.66:
        sign = ""
    if score >=60:
        sign = "-"
else:
    grade = "F"

print(f'Your grade is: {grade}{sign}')