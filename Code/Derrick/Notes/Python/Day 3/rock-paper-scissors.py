import random
import string

def rpsGame(user,computer):
    printMsg = (f'I chose {computer}, ')
    lose = ' you lose.'
    win = ' you win.'

    if user == computer:
        print(f'I chose {computer}, TIE')
    elif user == 'rock':
        if computer == 'paper':
            print(printMsg + lose)
        elif computer == 'scissors':
            print(printMsg + win)
    elif user == 'paper':
        if computer == 'scissors':
            print(printMsg + lose)
        elif computer == 'rock':
            print(printMsg + win)
    elif user == 'scissors':
        if computer == 'rock':
            print(printMsg + lose)
        elif computer == 'paper':
           print(printMsg + win)

again = 'y'
choices = ['rock','paper','scissors']

while again == 'y':
    userChoice = input('Choose Rock, Paper or Scissors: ').lower()
    computerChoice = random.choice(choices)
    rpsGame(userChoice,computerChoice)
    again = input('Would you like to play Rock, Paper, Scissors again(y/n)?')
