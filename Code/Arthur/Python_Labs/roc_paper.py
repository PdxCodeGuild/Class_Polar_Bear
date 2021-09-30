# # #part 1
import random

# #computer asks the user for choice


user_choice = input("Enter rock, paper or scissors: ")
user_choice=user_choice.lower()

# #computer randomly choses rock, paper or scissors
# random_number = random.randint(0,2)

available = ['rock','paper','scissors']
computer_choice=random.choice(available)

#picking computer choices 
# if random_number == 0:
#     computer_choice ="rock"
# elif random_number ==1:
#     computer_choice ="paper"
# elif random_number ==2:
#     computer_choice ="scissors"


if user_choice == computer_choice:
      print(f"This is a tie")
elif user_choice == "rock" :
       if computer_choice == "paper" :
         print(f"The computer wins!")
       else:
           print(f"you win!")
elif user_choice == "paper" :
    if computer_choice == "scissors" :
         print(f"The computer Wins!")
    else:
        print(f"you win")
elif user_choice == "scissors":
    if computer_choice =="rock":
        print(f"The computer wins!")
    else:
        print(f"You win")
else:
    print("Thank you for playing,Goodbye")

     
      


# # #part 2
# import random
# # #computer asks the user for choice

# user_choice = False

# while user_choice ==False:
#     available = ['rock','paper','scissors']
#     computer_choice=random.choice(available)
#     user_choice = input("Enter rock, paper or scissors: ")
#     if user_choice == computer_choice:
#       print(f"This is a tie")
#     elif user_choice == "rock" :
#        if computer_choice == "paper" :
#          print(f"The computer wins!")
#        else:
#            print(f"you win!")
#     elif user_choice == "paper" :
#        if computer_choice == "scissors" :
#          print(f"The computer Wins!")
#        else:
#         print(f"you win")
#     elif user_choice == "scissors":
#        if computer_choice =="rock":
#         print(f"The computer wins!")
#        else:
#         print(f"You win")
#     else:
#          print("Thank you for playing,Goodbye")
#     user_continue1 =input("Do you wish to continue?(yes/no)")
#     if user_continue1 == 'y':
#        user_choice = False
#     else:
#       print("Thank you for playing!!")
# user_choice =True

     
