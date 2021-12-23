# ---------------- #
# Python Lab 5 (rock, paper, scissors) 
# [revised, with French]
# 2021.12.13
# ---------------- #

# greeting and for loop to list selections

print('Welcome to Rock, Paper, Scissors (with bonus French vocabulary)! Your options are:')

selections = ['rock', 'paper', 'scissors']

for selection in selections:
    print(selection)

player_selection = input('Please enter your selection:')

import random

# program chooses a selection from the list

computer_selection = random.choice(selections)

# tie scenario

if player_selection == computer_selection:
    print('We have a tie. Ennuyant...')

# non-tie selection combinations, with French interjections

elif player_selection == 'rock':
    if computer_selection == 'paper':
        print('The computer wins. Quel dommage !')
    else:
        print('The player wins. Tous mes compliments !')

elif player_selection == 'rock':
    if computer_selection == 'scissors':
        print('The player wins. Tous mes compliments !')
    else:
        print('The computer wins. Quel dommage !')

elif player_selection == 'paper':
    if computer_selection == 'rock':
        print('The player wins. Tous mes compliments !')
    else:
        print('The computer wins. Quel dommage !')

elif player_selection == 'paper':
    if computer_selection == 'scissors':
        print('The computer wins. Quel dommage !')
    else:
        print('The player wins. Tous mes compliments !')

elif player_selection == 'scissors':
    if computer_selection == 'rock':
         print('The computer wins. Quel dommage!')
    else:
        print('The player wins. Tous mes compliments !')

elif player_selection == 'scissors':
    if computer_selection == 'paper':
        print('The player wins. Tous mes compliments !')
    else:
        print('The computer wins. Quel dommage!')

# ---------------- #