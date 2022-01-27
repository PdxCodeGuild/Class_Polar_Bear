# Authors #
    # James Thornton
    # Arthur Andama
    # Ryan Gaston
    # Chalie Ritter
    # Reece Adams

import random

pot = 0

def game_roll(playerindex, pot):
    # pot = 0
    player_roll = random.choice(game_choices)
    if player_roll == 'L':
        player_list[playerindex]['chips'] -= 1
        rewarded_player = playerindex - 1
        player_list[rewarded_player]['chips'] += 1
    elif player_roll == 'R':
        if playerindex + 1 == len(player_list):
            player_list[playerindex]['chips'] -= 1
            rewarded_player = 0
            player_list[rewarded_player]['chips'] += 1
        else:
            player_list[playerindex]['chips'] -= 1
            rewarded_player = playerindex + 1
            player_list[rewarded_player]['chips'] += 1
    elif player_roll == 'C':
        rewarded_player = playerindex - 1
        pot += 1
    return pot

player_list = [
]
choice = True
game_choices = ['L', 'C', 'R', 'Z', 'Z', 'Z']

while True:
    playernames = input('Enter your name, when all players have entered a anem type "done": ')
    if playernames == 'done':
        break
    else:
        player_list.append({'name':playernames, 'chips':3})

no_winner = True

while no_winner:
    for x in player_list:
        number_of_rolls = x['chips']
        if x['chips'] + pot == 12:
            print(f'{x} won with {x["chips"]} remaining!')
            no_winner = False
        for i in range(number_of_rolls):
            pot = game_roll(player_list.index(x), pot)