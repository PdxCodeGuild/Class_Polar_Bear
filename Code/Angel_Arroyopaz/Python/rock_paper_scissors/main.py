'''

Let's play rock-paper-scissors with the computer. 
You may want to try using these emojis 🗿📃✂️✊✋✌

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
Let's list all the cases:

rock vs rock (tie)
rock vs paper
rock vs scissors
paper vs rock
paper vs paper (tie)
paper vs scissors
scissors vs rock
scissors vs paper
scissors vs scissors (tie)


#  Version 2 (optional)

After playing, ask them if they'd like to play again. 
If they say yes, restart the game, otherwise exit.
'''

# import random module
import random

# while loop
while True:
    # explaining the game to the user
    print('''Hello and welcome. This is a Rock-Paper-Scissors game, and you'll be playing against me (the computer) \nRules are as follow: \n
    YOU  vs COMPUTER

    rock vs rock = Tie
    rock vs paper = Computer
    rock vs scissors = Human
    paper vs paper = Tie
    paper vs rock = Human
    paper vs scissors = Computer
    scissors vs scissors = Tie
    scissors vs rock = Computer
    scissors vs paper = Human''')

    # create list
    list = ["rock", "paper", "scissors"]

    print("\n")

    # display list

    for option in list:
        print(f"Option {list.index(option)} - {option}")

    print("\n")

    # user input
    user_input = input("Please select one option from the list above(i.e. rock): ")

    # convert user input to lowercase
    user_input = str.lower(user_input)
   
    print("\n")

    # computer gets a random choice
    computer = random.choice(list)

    # print the computers output
    print(f"Computer's choice is: {computer}")

    print("\n")
    
    # compare
    if user_input == computer:
        print("It's a tie!")

    elif user_input == "rock":
        if computer == "paper":
            print("You lost!")
        elif computer == "scissors":
            print("You won!")           

    elif user_input == "paper":
        if computer == "scissors":
            print("You lost!")
        elif computer == "rock":
            print("You won!")
            
    elif user_input == "scissors":
        if computer == "rock":
            print("You lost!")
        elif computer == "paper":
            print("You won!")
    
    print("\n")
    
    # we ask the user if they want to play again
    # If yes we restart the game
    # If not we break the loop and end the game
    play_again = input("Would you like to play again?(yes/no): ")
    play_again = str.lower(play_again)

    print("\n")
    
    if play_again == "yes":
        continue
    else:
        print("Thank you for playing! Goodbye!")
        break

    