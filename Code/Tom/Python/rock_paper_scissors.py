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
#Create counter and display options.
    counter=1
    for option in options:
        output=f'{counter}. {option}'
        print(output)
        counter+=1
        place='start'

#Users choice
    user=input('\nEnter your selection: ')
    user=user.title() #Capitalizes the response to match the options.

#Computer's choice
    computer=random.choice(options)

    result=results_check(user, computer)
    if result=='Invalid':
        print(f'\n{user} is an invalid selection. Try again.\n')
        continue
    else:
        print(f'User: {user}\nComputer: {computer}\n{result}\n')

    while True:
        try_again=input("Would you like to play again? y/n: ")
        if try_again=='n':
            loop=False
            break
        elif try_again=='y':
            loop=True
            break
        else:
            print(f'{try_again} is an invalid response. Would you like to play again? y/n: ')
            continue