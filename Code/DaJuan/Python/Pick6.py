#Pick 6 lotto lab
from math import exp
import random

def lotto():
    picks = []
    
    for num in range(6):
        digit = random.randint(1,99)
        picks.append(digit)
    return picks

#Should produce user picks
print(lotto())

def match(winner, picks):
    matches = 0

    for dig in range(len(winner)):
        if winner[d] == picks[d]:
            matches += 1

    return matches


prize_pool = {  1: 4, 2: 7, 3: 100, 4: 50_000, 5: 1_000_000, 6: 25_000_000}

losses = 0
winnings = 0

winner = lotto()

count = 0

while count < 100000:
    count += 1