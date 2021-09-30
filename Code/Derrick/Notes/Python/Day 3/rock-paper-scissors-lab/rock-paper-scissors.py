import random
import string
import rps

again = 'y'
choices = ['rock','paper','scissors']

while again == 'y':

    userChoice = input('Choose Rock, Paper or Scissors: ').lower()
    computerChoice = random.choice(choices)
    rps.game(userChoice,computerChoice)
    again = input('Would you like to play Rock, Paper, Scissors again(y/n)?')
    
    if again == 'n':
        print('See you next time')
