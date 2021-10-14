101.4 Rock Paper scissors

import random
def rockpapesciz():
    while True:
        selection = input('''Welcome to Rock, Paper, Scissors!

        Your options are:

        - Rock
        - Paper
        - Scissors

        Enter your selection:''')#<--#1 & 2

        choices = ["rock", "paper", "scissors"]
        computer_selection = random.choice(choices)#<---#3


        if selection == "rock":
            #Each combination of choices made
            if computer_selection == "scissors":
                print(f"You win! Opponent chose {choices[2]}.")
            elif computer_selection == "paper":
                print(f"You lose! Opponent chose {choices[1]}.")
        elif selection == "paper":
            if computer_selection == "rock":
                print(f"You win! Opponent chose {choices[0]}.")
            elif computer_selection == "scissors":
                print(f"You lose! Opponent chose {choices[2]}.")
        elif selection == "scissors":
            if computer_selection == "paper":
                print(f"You win! Opponent picked {choices[1]}.")
            elif computer_selection == "rock":
                print(f"You lose! Opponent chose {choices[0]}.")
                #Extra Challenge 1
        if selection == computer_selection:
            print("It's a TIE!")
#Extra Challenge
        def play_again():
            again = input("Play again? (y) or (n)")
            if again == "y":
                rockpapesciz()
            else:
                print("Goodbye.")

        play_again() 
        break         
rockpapesciz()

