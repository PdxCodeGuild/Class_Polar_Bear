'''Group participants name : Ken Mazur, Arthur Andama, Mark Wilson,Aaron Parker,Ryan Gaston'''

'''Using a `while` loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, 
the user is told they've lost. If the user guesses the number, the user is told they've won and the game exits. 
You can get a random number using random.randint:'''



# import random
# x = random.randint(1,10)

# counter = 0
# while counter <10:
#     user_number =int(input("Enter a number: "))
#     if user_number == x:
#         break
#     print(f"The number you entered is: {user_number}, Computer Guess :{x}")
#     counter +=1
# if counter == 10:
#     print("you failed.")
# else:
#     print("you won!")
# print(f"computer guess: {x}")

## Part 2

# '''Allow the user to make an unlimited number of guesses using a `while True` and `break`.
#  Keep track of how many guesses the user has made, and tell them at the end.'''

# import random
# x = random.randint(1,10)

# counter = 1
# while True:
#     user_number =int(input("Enter a number: "))
#     if user_number == x:
#         break
#     print(f"The number you entered is: {user_number}, Computer Guess :{x}")
#     counter +=1
# print(f"you guessed right. you guessed : {counter} times")


## Part 3

'''Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.'''

import random
x = random.randint(1,10)

counter = 1
while True:
    user_number =int(input("Enter a number: "))
    if user_number == x:
        break
    elif user_number < x:
        print("that guess is too low!")
    elif user_number > x:
        print("the guess is too high")
   
    # print(f"The number you entered is: {user_number}, Computer Guess :{x}")
    counter +=1
print(f"you guessed right. you guessed : {counter} times")