import random

#list of choices
choose = ['rock', 'paper', 'scissors']
while True:

    while True:

        game = input('Choose rock, paper, or scissors: ').lower().strip()
        if game in choose:
            break

    computer = random.choice(choose)
    print("computer chose" + computer)
    

        

    if game == computer:
        print('tie')
    elif game == 'rock' and computer == 'paper':
        print('Computer wins')
    elif game == 'rock' and computer == 'scissors':
        print('You win')
    elif game == 'paper' and computer == 'rock':
        print('You win')
    elif game == 'paper' and computer == 'scissors':
        print('Computer wins')
    elif game == 'scissors' and computer == 'rock':
        print('You lose')
    elif game == 'scissors' and computer == 'paper':
        print('You win')

    while True:
        play_again = input('Would you like to play again? yes / no: ')
        if play_again == 'yes' or 'no':
            break

    if play_again == 'no':

        break