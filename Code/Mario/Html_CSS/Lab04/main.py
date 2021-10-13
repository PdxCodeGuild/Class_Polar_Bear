

# x = random.randint(1, 10)
# counter = 0
# max_num = 10
# guessed_num = 0

# while True:
#     user_input = input(f'Guess a number between 1-{max_num}: ')
#     try:
#         user_input = int(user_input)
#     except ValueError:
#         print("That's not a valid number. Try again.")
#         continue
#     if user_input > max_num or user_input < 1:
#         print(f"That's invalid. Choice must be between 1-{max_num}")
#         continue
#     if counter == 10:
#         print("You've guessed 10 times. Thank you for trying!")
#         break
#     if user_input != x:
#         if counter == 0:
#             if user_input < x:
#                 print("Too low.")
#             else:
#                 print("Too high")
#         else:
#             if abs(user_input - x) < abs(guessed_num - x):
#                 print("You're getting closer")
#             else:
#                 print("You are getting further")
#         counter += 1
#         guessed_num = user_input
#     else:
#         print("Congratulations!!!")
#         break

import random


user_choice = int(input("Pick a number between 1-5: "))
while True:
    computer = random.randint(1, 5)
    print(computer)
    if computer == user_choice:
        print("Computer wins")
        break
    else:
        print("Guessing...")
