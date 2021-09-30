import random
choices = ['rock', 'paper', 'scissors']
clear = [' ', ' ', ' ']
for cleared in clear:
    print(f' ')
print(f'----------Welcome to Rock, Paper, Scissors.----------')
while True:
    number = 1
    for cleared in clear:
        print(f' ')
    print('Please choose one of the following: ')
    for choice in choices:
        print(f'{number}. {choice}')
        number = number + 1
    print('4. done (to quit)')
    human_choice = input('Your choice: ').lower()
    computer_choice = random.choice(choices)
    print(f'Computer chose: {computer_choice}')

    if human_choice == computer_choice:
        print('You have tied!')
    elif human_choice == 'rock':
        if computer_choice == 'paper':
            print('You lost')
        else:
            print('You win')
    
    elif human_choice == 'paper':
        if computer_choice == 'scissors':
            print('You lost')
        else:
            print('You win')

    elif human_choice == 'scissors':
        if computer_choice == 'rock':
            print('You lost')
        else:
            print('You win')
    elif human_choice == 'done':
        print('Thanks for playing')
        for cleared in clear:
            print(f' ')
        break
    else:
        print('Please make sure you spelled your {choices} correctly.')

#--------------This was a longer way to do the same thing

    # if human_choice == 'rock' and computer_choice == 'rock':
    #     print('Tie')
    # elif human_choice == 'rock' and computer_choice == 'paper':
    #     print('Compuer Wins')
    # elif human_choice == 'rock' and computer_choice == 'scissors':
    #     print('You Win')
    # elif human_choice == 'paper' and computer_choice == 'rock':
    #     print('You Win')
    # elif human_choice == 'paper' and computer_choice == 'paper':
    #     print('Tie')
    # elif human_choice == 'paper' and computer_choice == 'scissors':
    #     print('Computer Wins')
    # elif human_choice == 'scissors' and computer_choice == 'rock':
    #     print('Computer Wins')
    # elif human_choice == 'scissors' and computer_choice == 'paper':
    #     print('You Win')
    # elif human_choice == 'scissors' and computer_choice == 'scissors':
    #     print('Tie')
    # elif human_choice == 'done':
    #     print('Thanks for playing!')
    #     break
    # else:
    #     print('Please make sure you spelled your {choices} correctly.')

# if human_choice > computer_choice:
#     print('You win!')
# elif human_choice == computer_choice:
#     print('Tie')
# elif human_choice < computer_choice:
#     print('Computer wins!')
# else:
#     print('Please enter rock, paper, or scissors (lower case) only: ')