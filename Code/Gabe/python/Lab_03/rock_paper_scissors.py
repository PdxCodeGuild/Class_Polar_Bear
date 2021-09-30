import random

choices = ['rock', 'paper', 'scissors']


while True:
  user_choice = input(f'\nEnter choice between {choices[0]}, {choices[1]}, or {choices[2]}: ')
  computer_choice = random.choice(choices)
  print(computer_choice)
  try:
    type(user_choice) == str
  except:
    print('bad choice')
    exit()

  if user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors':
    print(f'\nPlease choose between {choices[0]}, {choices[1]}, or {choices[2]}, Try Again! ')
    continue

  if user_choice == 'rock' and computer_choice == 'scissors':
    print('You Win')
  elif user_choice == 'paper' and computer_choice == 'rock':
    print('You Win')
  elif user_choice == 'scissors' and computer_choice == 'paper':
    print('You Win')
  elif computer_choice == 'rock' and user_choice == 'scissors':
    print('Computer Wins')
  elif computer_choice == 'paper' and user_choice == 'rock':
    print('Computer Wins')
  elif computer_choice == 'scissors' and user_choice == 'paper':
    print('Computer Wins')
  else:
    print('Tie!')

  play_again = input('\nWould you like to play again? y/n: ')

  if play_again == 'n' or play_again == 'no':
    break
  else:
    continue