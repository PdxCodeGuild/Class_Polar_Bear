'''
Full-Stack
Rock, Paper, Scissors Lab
'''

import random

options=['Rock', 'Paper', 'Scissors']
loop=True


def results_check(user_input, computer_input):
    if user_input=='Rock' and computer_input=='Scissors':
        return 'Win!'
    elif user_input=='Paper' and computer_input=='Rock':
        return 'Win!'
    elif user_input=='Scissors' and computer_input=='Paper':
        return 'Win!'
    elif user_input=='Paper' and computer_input=='Scissors':
        return 'Lose!'
    elif user_input=='Scissors' and computer_input=='Rock':
        return 'Lose!'
    elif user_input=='Rock' and computer_input=='Paper':
        return 'Lose!'
    elif user_input==computer_input: #catches any ties
        return 'Tie!'
    else: #catches all other results
        return 'Invalid'

Welcome='\nWelcome to Rock, Paper, Scissors!\n\nYour options are:\n'
print(Welcome)

while loop==True:
#Create counter and display options
    counter=1
    for option in options:
        output=f'{counter}. {option}'
        print(output)
        counter+=1

#Users choice
    user=input('\nEnter your selection: ').title()

#Computer's choice
    computer=random.choice(options)

    result=results_check(user, computer)
    if result=='Invalid':
        print(f'\n"{user}" is an invalid selection. Try again.\n')
        continue
    else:
        print(f'User: "{user}"\nComputer: "{computer}"\n{result}\n')

    while True:
        try_again=input("Would you like to play again? (Yes/No): ").title()
        if try_again=='N' or try_again=='No':
            loop=False
            break
        elif try_again=='Y' or try_again=='Yes':
            loop=True
            break
        else:
            print(f'\n"{try_again}" is an invalid response.')
            continue