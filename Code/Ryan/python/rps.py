import random
choices = ['rock', 'paper', 'scissors']
user_wins = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}

print('\n\n\n\nWelcome to Rock, Paper, Scissors!\n\nTo play, please type the word from the following options: ')
user_choice = 'none'
number = 1
for choice in choices:
    print(f'{number}. {choice}')
    number = number + 1
# user_choice = input('\nEnter your choice: ').lower()
round = 1

while user_choice != 'done':
    if round >= 2:
        number = 1
        print(f'You can play again or quit by entering one of the following options:')
        for choice in choices:
            print(f'{number}. {choice}')
            number = number + 1
        print(f'{number}. done (for quit)\n')
    user_choice = input('Enter your choice: ').lower()
    computer_choice = random.choice(choices)

    if user_choice == 'done':
        break
    elif user_choice not in choices:
        print('Please check your spelling and enter: \n')
        number = 1
        for choice in choices:
            print(f'{number}. {choice}')
            number = number + 1
        print(f'{number}. done (to quit)\n')
        round = 0

    elif user_choice == computer_choice:
        print(f'\nComputer chose {computer_choice}\n')
        print("It's a tie!\n")

    else:
        computer_lose = user_wins[user_choice]
        print(f'\nComputer chose {computer_choice}\n')
        if computer_choice == computer_lose:
            print(f'You won, {user_choice} beats {computer_choice}!\n')
        else:
            print(f'You lose, {computer_choice} beats {user_choice}!\n')
    round = round + 1


# message = ''' This is a 
# multiline string.
# Kinda cool right?'''
# print(message)