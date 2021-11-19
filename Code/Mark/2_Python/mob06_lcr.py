import random

while True:
    players = []
    while True:
        player_name = input('Please enter the player name, or \'done\' to start the game: ')
        if player_name == 'done':
            break
        players.append({'name': player_name, 'chips': 3})
    
    # [{'name': 'alpha','chips': 3}, {'name': 'beta','chips': 3}, {'name': 'delta','chips': 3}, {'name': 'gamma','chips': 3}]

    pot = 0
    while True:
        for i in range(len(players)): # 0, 1, 2, 3
            number_of_dice = min(3, players[i]['chips'])
            for _ in range(number_of_dice):
                x = random.randint(1,6)
                if x == 1: # equivalent to L (add to the left)
                    players[i]['chips'] -= 1
                    players[i-1]['chips'] += 1
                elif x == 2: # equivalent to C (add to the pot)
                    players[i]['chips'] -= 1
                    pot += 1
                elif x == 3: # equivalent to R (add to the right)
                    players[i]['chips'] -= 1
                    players[(i+1)%len(players)]['chips'] += 1
        
        count = 0
        winner = ''
        for player in players:
            if player['chips'] > 0:
                count += 1
                winner = player['name']
        if count == 1:
            print(f'The winner is {winner}')
            break
    
    if input('Do you want to play again? Y or N? ') == 'N':
        break
