
# Each player begins with 3 chips. Players take turns rolling three six-sided dice, each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.

# If a player has fewer than three chips left, they're still in the game but their number of chips is the number of dice they roll on their turn, rather than rolling all three. When a player has zero chips, they pass the dice on their turn, but may receive chips from others and take their next turn accordingly. The winner is the last player with chips left, and wins the center pot.

# When the program starts, it should ask for the names of the players, until the user enters 'done'. Then it should run the simulation, tell the user who won, and ask the player whether they'd like to play again. We can represent the players as a list of dictionaries with each dictionary containing two key-value pairs: player's name and the number of chips they have, e.g. {'name': 'Billy', 'chips': 3}.
import random

players = []
pot = 0
dice = ['L','C','R',1,1,1]

def addPlayer(name,chipCount):
    players.append({'name': name,'chips': chipCount})

def rollDice(n):
    outcome = []

    for i in range(n):
        outcome.append(random.choice(dice))

    return outcome

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
    
        

while True:
    name = input('Please enter player name or \'done\' to continue to the game: ')

    if name == 'done':
        break

    addPlayer(name,3)
       

chipCounts = []

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
            

    for i in range(len(chipCounts)):
        chipCounts[i] = players[i]['chips']
            
    if chipCounts.count(0) == len(chipCounts) - 1:
        for i in range(len(players)):
            if players[i]['chips'] > 0:
                print('The winner is ' + players[i]['name'] + ' who is holding ' + str(players[i]['chips']) + ' chip(s)')
        break
    
print(players)

