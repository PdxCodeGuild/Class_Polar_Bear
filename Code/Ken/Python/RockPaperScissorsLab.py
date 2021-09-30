import random

#List
selections = [
    "rock", 
    "paper", 
    "scissors"
]

print("Welcome to Rock, Paper, Scissors!  Your options are: ")

# Loop

for selection in selections:
	print(f" - {selection}")

# User Input

user_selection = input("Enter your selection: ")

#Random computer choice

computer_selection = random.choice(selections)

print(f"I choose: {computer_selection}")

# Game on

if user_selection == computer_selection:
	output="We have a Tie Game!"

elif user_selection == "rock" and computer_selection == "paper":
	output="Paper covers rock, therefore I win"

elif user_selection == "rock" and computer_selection == "scissors":
	output="Rocks breaks Scissors, therefore you win"

elif user_selection == "paper" and computer_selection == "rock":
    output="Paper covers Rocks, therefore you win"

elif user_selection == "paper" and computer_selection == "scissors":
    output="Scissors cuts Paper, therefore I win"

elif user_selection == "scissors" and computer_selection == "rock":
    output="Rocks breaks Scissors, therefore I win"

else:
     output="Scissors cuts Paper, therefore you win"

print(output)