import random
print('Welcome to Rock, Paper, Scissors!\n\nYour options are:\n')
c1, c2, c3 = 'rock', 'paper', 'scissors'
choices = {c1:c3, c2:c1, c3:c2}
for c in choices.keys():
    print(f'- {c}')
player = input('\nEnter your selection: ')
print()
computer = random.choice(list(choices.keys()))
if computer == player:
    print('It\'s a tie!')
elif player not in choices.keys():
    print('Invalid selection.')
else:
    print(f'The computer chose {computer}.')
    lose = choices[player]
    if computer == lose:
        print(f'You won, {player} beats {computer}!')
    else:
        print(f'You lose, {computer} beats {player}!')

