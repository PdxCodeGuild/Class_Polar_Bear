'''# Rock Paper Scissors

Let's play rock-paper-scissors with the computer. 
You may want to try using these emojis 🗿📃✂️✊✋✌

1. The computer will ask the user for their choice (rock, paper, scissors)
2. The computer will randomly choose rock, paper or scissors
3. Determine who won and tell the user

Let's list all the cases:
- rock vs rock (tie)
- rock vs paper
- rock vs scissors
- paper vs rock
- paper vs paper (tie)
- paper vs scissors
- scissors vs rock
- scissors vs paper
- scissors vs scissors (tie)

## Version 2 (optional)

After playing, ask them if they'd like to play again. If they say yes, 
restart the game, otherwise exit.'''
'''Using a `while` loop, allow the user to guess 10 times. 
If they fail to guess the number after 10 tries, 
the user is told they've lost.
 If the user guesses the number, 
 the user is told they've won and the game exits. 
You can get a random number using random.randint:'''


# import random


# # 

# # print("\U0001FAA8")
# # print("\U0001F590")
# # print("\U0000270C")
# # print("\U0000270B")

# # rock = '\U0000270A'
# # paper ='\U0001F9FB'
# # scissors ='\U00002702'

# available = ['rock', 'paper','scissors']

# #ask for a user choice
# # user_choice =input(f"Enter {rock},{paper} or {scissors}")
# user_choice =input(f"Enter rock,paper or scissors : ")
# #computer picks a random choice
# computer_choice = random.choice(available)
# if user_choice == computer_choice:
#     print(f"It's a Tie")
# elif user_choice == 'rock':
#     if computer_choice == 'paper':
#         print(f"The computer wins :")
#     else:
#         print(f"You win!")
# elif user_choice == 'paper':
#     if computer_choice == 'scissors':
#            print(f"The computer wins")
#     else:
#         print(f"You win!")

# elif user_choice == 'scissors':
#     if computer_choice == 'rock':
#            print("The computer wins :")
#     else:
#         print(f"You win! ")

# else:
#     print("Invalid choice:")

    

# '''## Version 2 (optional)

# After playing, ask them if they'd like to play again. If they say yes, 
# restart the game, otherwise exit.'''
# import random

# # print("\U0001FAA8")
# # print("\U0001F590")
# # print("\U0000270C")
# # print("\U0000270B")

# # rock = '\U0000270A'
# # paper ='\U0001F9FB'
# # scissors ='\U00002702'
# available = ['rock', 'paper','scissors']
# play_again = False
# #ask for a user choice
# while play_again == False :
#     user_choice =None
#     while user_choice not in available:
#         # user_choice =input(f"Enter {rock},{paper} or {scissors}")
#         user_choice =input(f"Enter rock,paper or scissors : ")
#     #computer picks a random choice
#     computer_choice = random.choice(available)
#     if user_choice == computer_choice:
#        print(f"It's a Tie")
#     elif user_choice == 'rock':
#       if computer_choice == 'paper':
#         print(f"The computer wins :")
#       else:
#         print(f"You win!")
#     elif user_choice == 'paper':
#         if computer_choice == 'scissors':
#            print(f"The computer wins")
#         else:
#            print(f"You win!")

#     elif user_choice == 'scissors':
#          if computer_choice == 'rock':
#            print("The computer wins :")
#          else:
#             print(f"You win! ")

#     else:
#            print("Invalid choice:")


#part3

import random

# print("\U0001FAA8")
# print("\U0001F590")
# print("\U0000270C")
# print("\U0000270B")

# rock = '\U0000270A'
# paper ='\U0001F9FB'
# scissors ='\U00002702'
available = ['rock', 'paper','scissors']
play_again = False
#ask for a user choice
while play_again == False  :
    user_choice =None
    while user_choice not in available:
        # user_choice =input(f"Enter {rock},{paper} or {scissors}")
        user_choice =input(f"Enter rock,paper or scissors : ")
        user_choice.lower()
    #computer picks a random choice
    computer_choice = random.choice(available)
    if user_choice == computer_choice:
       print(f"It's a Tie")
    elif user_choice == 'rock':
      if computer_choice == 'paper':
        print(f"The computer wins :")
      else:
        print(f"You win!")
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
           print(f"The computer wins")
        else:
           print(f"You win!")

    elif user_choice == 'scissors':
         if computer_choice == 'rock':
           print("The computer wins :")
         else:
            print(f"You win! ")
    else:
           print("Invalid choice:")

    user_choice1=input("Would you like to play again? y/n: ")
    if user_choice1 =='yes':
        play_again = False
    else:
        #or use break
        play_again == True
          # break
    print("Good bye. Till next time")



      
          

      
        

