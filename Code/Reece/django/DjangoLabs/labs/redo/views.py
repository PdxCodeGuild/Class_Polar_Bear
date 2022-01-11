from django.shortcuts import render
import random
# Create your views here.

def rps_choice(request):
    return render(request, 'redo/index.html')
#-
rps_options = [
        'rock',
        'paper', 
        'scissors'
        ]
#-rps_rock
def rps_rock(request):
    user_sel = 'rock'

    comp_sel = random.choice(rps_options)

    if comp_sel == user_sel:
        game_msg = f'\tTie! You chose {user_sel} and tied with {comp_sel}.'
    elif comp_sel == 'scissors':
        game_msg = f'\tWinner! You chose {user_sel} and beat {comp_sel}.'
    elif comp_sel == 'paper':
        game_msg = f'\tLoser! You chose {user_sel} and lost to {comp_sel}.'

    return render(request, 'redo/results.html', {'game_msg':game_msg})
#-rps_paper
def rps_paper(request):
    user_sel = 'paper'

    comp_sel = random.choice(rps_options)

    if comp_sel == user_sel:
        game_msg = f'\tTie! You chose {user_sel} and tied with {comp_sel}.'
    elif comp_sel == 'rock':
        game_msg = f'\tWinner! You chose {user_sel} and beat {comp_sel}.'
    elif comp_sel == 'scissors':
        game_msg = f'\tLoser! You chose {user_sel} and lost to {comp_sel}.'

    return render(request, 'redo/results.html', {'game_msg':game_msg})
#-rps_scissors
def rps_scissors(request):
    user_sel = 'scissors'

    comp_sel = random.choice(rps_options)

    if comp_sel == user_sel:
        game_msg = f'\tTie! You chose {user_sel} and tied with {comp_sel}.'
    elif comp_sel == 'paper':
        game_msg = f'\tWinner! You chose {user_sel} and beat {comp_sel}.'
    elif comp_sel == 'rock':
        game_msg = f'\tLoser! You chose {user_sel} and lost to {comp_sel}.'

    return render(request, 'redo/results.html', {'game_msg':game_msg})