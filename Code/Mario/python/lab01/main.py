
# symbol = {
#     "0.97": "+",
#     "0.": "-"
# }

# number_grade = int(input('Enter a number from 0-100: '))


score = 0
result = ''

while True:
    number_grade = int(input('Enter a number from 0-100: '))
    if number_grade <= 59:
        result = f'Score of {number_grade} is : F'
        score = round(number_grade / 59, 2)
    elif number_grade >= 60 and number_grade <= 69:
        result = f'Score of {number_grade} is : D'
        score = round(number_grade / 69, 2)
    elif number_grade >= 70 and number_grade <= 79:
        result = f'Score of {number_grade} is : C'
        score = round(number_grade / 79, 2)
    elif number_grade >= 80 and number_grade <= 89:
        result = f'Score of {number_grade} is : B'
        score = round(number_grade / 89, 2)
    else:
        result = f'Score of {number_grade} is : A'
        score = round(number_grade / 99, 2)

    if score <= 0.88 and number_grade > 59:
        print(f"{result}"+"-")
    elif score >= 0.9 and score <= 0.94 and number_grade > 59:
        print(result)
    elif number_grade > 59:
        print(f"{result}" + "+")
    print(score)
