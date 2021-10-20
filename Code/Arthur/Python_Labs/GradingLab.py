'''# Grading

## Part 1

convert a number grade to a letter grade, 
using `if` and `elif` statements and comparisons. 
First have the user enter a number representing the grade (0-100). 
Then convert the number grade to a letter grade.

Concepts Covered:
- `fundamentals`, `comparisons & conditionals`
Numeric Ranges:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- 0-59: F

## Part 2

Find the specific letter grade (A+, B-, etc). 
You can check for more specific ranges using `if` statements, 
or use modulus `%` to get the ones-digit to 
set another string to `'+'`, `'-'`, or `' '`. 
Then you can concatenate that string with your grade string. 

'''

# #part1
# #we prompt by asking the user to enter a number between 0 to 100
# user_number = input("Enter a number between 0 & 100 : ")

# #we validate what the user entered in a try and catch to make sure a user enters only a value
# try :
#     user_number = float(user_number)
#     if user_number > 100 or user_number<0:
#         #you can also use break
#         raise ValueError
# except ValueError:
#     print("Invalid choice or grade .. Goodbye")
#     exit()

# #check if the number confirms to standard and user it to generate the letter grade.
# if user_number >=90 or user_number <= 100:
#  print(f"Letter Grade is : A")
# elif user_number>=89 or user_number<=80:
#  print(f"Letter Grade : B")
# elif user_number>=70 or user_number<=79:
#  print(f"Letter Grade is : C")
# elif user_number>=60 or user_number<=69:
#  print(f"Letter Grade is : D")
# else :
#  print(f"Letter Grade is : F")



 #part2
 #we prompt by asking the user to enter a number between 0 to 100
user_number = input("Enter a number between 0 & 100 : ")

#we validate what the user entered in a try and catch to make sure a user enters only a value
try :
    user_number = float(user_number)
    if user_number > 100 or user_number<0:
        #you can also use break
        raise ValueError
except ValueError:
    print("Invalid choice or grade .. Goodbye")
    exit()
#this generates + plus or -
Letter_grade = None
ones_digit = user_number%10
if ones_digit==9:
    user_number =round(user_number)

#check if the number confirms to standard and user it to generate the letter grade.
if user_number >=90 and user_number <= 100:
 Letter_grade ="A"
elif user_number>=80:
 Letter_grade ="B"
elif user_number>=70:
 Letter_grade ="C"
elif user_number>=60:
 Letter_grade ="D"
else :
 Letter_grade ="F"


#checking more specific using the one digit
if user_number>=60:
    #we can say that 7 or greater is a +
    if ones_digit >=7 or user_number>=70:
        #Letter_grade +="+"
        Letter_grade += "+"
    #we check 3 or below is -
    elif ones_digit <=3 :
        Letter_grade += "-"

#showing the final input
print(f"Your grade is {user_number} results are in {Letter_grade}")

