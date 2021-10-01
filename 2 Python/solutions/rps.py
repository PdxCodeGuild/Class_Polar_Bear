import random

available_choices = ['rock', 'paper', 'scissors']
play_again = False
while play_again == False:
    user_choice = None
    while user_choice not in available_choices:
        user_choice = input("Choose: Rock, Paper, Scissors... ")
        user_choice = user_choice.lower()

    computer_choice = random.choice(available_choices)

    if user_choice == computer_choice:
        print("It is a tie")
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print('Computer wins :(')
        else:
            print('You win!')
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            print('Computer Wins :(')
        else:
            print('You win!')
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print('Computer Wins :(')
        else:
            print('You win!')
    else:
        print('Invalid option')

    user_choice1 = input('Do you want to play again? (y/n): ')
    if user_choice1 == 'yes':
        play_again = False
    else:
        print('Thank you for playing, goodbye')
        play_again = True