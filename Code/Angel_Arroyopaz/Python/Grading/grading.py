'''
# PART 1

Let's convert a number grade to a letter grade, using if and elif statements and comparisons. 
First have the user enter a number representing the grade (0-100). 
Then convert the number grade to a letter grade.

# PART 2

Find the specific letter grade (A+, B-, etc). You can check for more specific ranges using if statements,
or use modulus % to get the ones-digit to set another string to '+', '-', or ' '.
Then you can concatenate that string with your grade string.
'''

# we import math and string module
import math

# we welcome the users and explain how this program works
print("Hello and welcome, to find out what letter grade you got \nin this class follow the instructions bellow.\n")


# We loop this to make sure the user inputs a valid number

while True:

    # we ask the users to enter their score
    user_input = input("Enter your score (0-100): ")

    try:
        user_input = int(user_input)
    except ValueError:
        print("That was not a number. Try again")
        continue

    if user_input >= int(101) or user_input <= int(-1):
        print("Invalid number. Try again")

    else:
        break

# we convert input default str to a float so we can use that input
# in our conditionals later
user_input = float(user_input)

print("\n")

# we convert the users score to a letter grade ranging from A to F
'''
The numberic ranges are as follow:

90-100: A
80-89: B
70-79: C
60-69: D
0-59: F
'''

# we divide the users input by 10 to determine if the user gets a + or -
# append to the end of their grade
user_input_extra = user_input % 10

# we create a conditional where if the users input is equal or greater than 90
# then we print the letter grade 'A'
if user_input >= 90:
    # we call the variable user_input_extra inside of the following  if statement
    # to determine if the user gets a + or - append to their letter grade
    if user_input_extra >= 5:
        print("You got an \033[1m'A +'\033[0m, congratulations!")
    elif user_input_extra >= 0:
        print("You got an \033[1m'A -'\033[0m, congratulations!")
# from here down we create additional conditionals for the rest of the values and
# print the corresponding letter grade to each condition    
elif user_input >= 80:
    if user_input_extra >= 5:
        print("You got an \033[1m'B +'\033[0m, congratulations!")
    elif user_input_extra >= 0:
        print("You got an \033[1m'B -'\033[0m, congratulations!")

elif user_input >= 70:
    if user_input_extra >= 5:
        print("You got an \033[1m'C +'\033[0m, congratulations!")
    elif user_input_extra >= 0:
        print("You got an \033[1m'C -'\033[0m, congratulations!")
    
elif user_input >= 60:
    if user_input_extra >= 5:
        print("You got an \033[1m'D +'\033[0m, congratulations!")
    elif user_input_extra >= 0:
        print("You got an \033[1m'D -'\033[0m, congratulations!")
    
else:
    print("You got an \033[1m'F'\033[0m, congratulations!")


