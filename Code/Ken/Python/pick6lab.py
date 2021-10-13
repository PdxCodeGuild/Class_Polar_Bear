import random



def pick6():
    numbers = []
    for i in range(0, 6):
        numbers.append(random.randint(1, 100))
    return numbers

lottery_draw = pick6()




def game():

    draws = 100000
    balance = 0
    winnings = 0
    costs = 0
    match_one = 0
    match_two = 0
    match_three = 0
    match_four = 0
    match_five = 0
    jackpot = 0

    for x in range(draws):
        balance -= 2
        costs -= 2
        pick = pick6()
        number_matches = 0
        
        for num in range(len(pick)):
            if pick[num] == lottery_draw[num]:
                number_matches += 1

        if number_matches == 1:
            balance += 4
            winnings += 4
            match_one += 1
        elif number_matches == 2:
            balance += 7
            winnings += 7
            match_two += 1
        elif number_matches == 3:
            balance += 100
            winnings += 100
            match_three += 1
        elif number_matches == 4:
            balance += 50000
            winnings += 50000
            match_four += 1
        elif number_matches == 5:
            balance += 1000000
            winnings += 1000000
            match_five += 1
        elif number_matches == 6:
            balance += 25000000
            winnings += 25000000
            jackpot += 1

        ROI = (winnings - costs) / costs
    return (f'You won ${winnings} and you spent ${costs}.   Your ROI is: {ROI}')

print(game())

