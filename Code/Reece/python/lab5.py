import random


rps_choice = [
    'rock',
    'paper', 
    'scissors'
    ]
prnt_list = (', '.join(map(str, rps_choice)))
game = True

while game == True:
    user_sel = input(f'\nWelcome to Rock, Paper, Scissors. Your choices are {prnt_list}.\n\n Please enter your choice here: ').lower()
    while user_sel not in rps_choice:
        user_sel = input(f'\n\tInavlid Choice...Choose rock, paper, or scissors: ').lower()
    comp_sel = random.choice(rps_choice)
    if user_sel == 'rock':
        if comp_sel == 'paper':
            game_msg = f'\tLoser! You chose {user_sel} and lost to {comp_sel}.'
        elif comp_sel == 'scissors':
            game_msg = f'\tWinner! You chose {user_sel} and beat {comp_sel}.'
        elif comp_sel == 'rock':
            game_msg = f'\tTie! You chose {user_sel} and tied with {comp_sel}.'
    elif user_sel == 'paper':
        if comp_sel == 'paper':
            game_msg = f'\tTie! You chose {user_sel} and tied with {comp_sel}.'
        elif comp_sel == 'scissors':
            game_msg = f'\tLoser! You chose {user_sel} and lost to {comp_sel}.'
        elif comp_sel == 'rock':
            game_msg = f'\tWinner! You chose {user_sel} and beat {comp_sel}.'
    elif user_sel == 'scissors':
        if comp_sel == 'paper':
            game_msg = f'\tWinner! You chose {user_sel} and beat {comp_sel}.'
        elif comp_sel == 'scissors':
            game_msg = f'\tTie! You chose {user_sel} and tied with {comp_sel}.'
        elif comp_sel == 'rock':
            game_msg = f'\tLoser! You chose {user_sel} and lost to {comp_sel}.'
    print(game_msg)
    replay_var = input('\nEnter "yes" to replay or just press ENTER to exit: ')
    if replay_var == 'yes':
        print(f'\nReplay Initializing...')
        game = True
        continue
    else:
        print('\tThanks for playing!')
        game = False
        break

# Part 1 ----------------------------------------------------- #
# rps_choice = [
#     'rock',
#     'paper', 
#     'scissors']
# prnt_list = (', '.join(map(str, rps_choice)))
# user_sel = input(f'\nWelcome to Rock, Paper, Scissors. Your choices are {prnt_list}.\n\n Please enter your choice here: ').lower()
# comp_sel = random.choice(rps_choice)
# game_msg = ''

# if user_sel == 'rock':
#     if comp_sel == 'rock':
#         game_msg = f'\nYou tied! You chose {user_sel} tying with {comp_sel}!\n'
#     elif comp_sel == 'paper':
#         game_msg = f'\nYou lost! You chose {user_sel} losing to {comp_sel}!\n'
#     elif comp_sel == 'scissors':
#         game_msg = f'\nYou won! You chose {user_sel} beating {comp_sel}!\n'
# elif user_sel == 'paper':
#     if comp_sel == 'rock':
#         game_msg = f'\nYou won! You chose {user_sel} beating {comp_sel}!\n'
#     elif comp_sel == 'paper':
#         game_msg = f'\nYou tied! You chose {user_sel} tying with {comp_sel}!\n'
#     elif comp_sel == 'scissors':
#         game_msg = f'\nYou lost! You chose {user_sel} losing to {comp_sel}!\n'
# elif user_sel == 'scissors':
#     if comp_sel == 'rock':
#         game_msg = f'\nYou lost! You chose {user_sel} losing to {comp_sel}!'
#     elif comp_sel == 'paper':
#         game_msg = f'\nYou won! You chose {user_sel} beating {comp_sel}!\n'
#     elif comp_sel == 'scissors':
#         game_msg = f'\nYou tied! You chose {user_sel} tying with {comp_sel}!\n' 

# print(game_msg)