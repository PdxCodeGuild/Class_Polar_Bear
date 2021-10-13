import random

players = []
chipCounts = []
pot = 0
dice = ['L','C','R',1,1,1]

# add players objects to players list
def addPlayer(name,chipCount):
    players.append({'name': name,'chips': chipCount})

# roll dice and create temporary list 
def rollDice(n):
    outcome = []

    for i in range(n):
        outcome.append(random.choice(dice))

    return outcome

# checks temporary list for L C or R and performs the appropriate actions
def diceCheck():
    if 'L' in x:
        players[i]['chips'] -= 1
        players[i - 1]['chips'] += 1

    if 'C' in x:
        players[i]['chips'] -= 1
        global pot
        pot += 1

    if 'R' in x:
        players[i]['chips'] -= 1

        if players[i] == players[-1]:
            players[0]['chips'] += 1

        else:
            players[i + 1]['chips'] += 1


# ask user for player names
while True:
    name = input('Please enter player name or \'done\' to continue to the game: ')

    if name == 'done':
        break

    addPlayer(name,3)


# create initial chip count 
for i in range(len(players)):
    chipCounts.append(players[i]['chips'])


while chipCounts.count(0) != len(chipCounts) - 1:
    
    for i in range(len(players)):
        
        if players[i]['chips'] > 3:
            x = rollDice(3)
            diceCheck()
            
        else:
            x = rollDice(players[i]['chips'])
            diceCheck()
            
    # update chipCount list 
    for i in range(len(chipCounts)):
        chipCounts[i] = players[i]['chips']

    # to compare chip counts and verify if only 1 player still has chips        
    if chipCounts.count(0) == len(chipCounts) - 1:
        for i in range(len(players)):
            if players[i]['chips'] > 0:
                print('The winner is ' + players[i]['name'] + ' who is holding ' + str(players[i]['chips']) + ' chip(s)')
        break
    
print(players)

