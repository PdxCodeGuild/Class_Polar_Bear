import random 

cards = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,    
}

playerCards = {
    'firstCard': input('What is your first card'),
    'secondCard': input('What is your second card'),
    'thirdCard': input('What is your third card?')
}

def printTotal(msg):
    print(msg)

def hitStayBust(n):
    if n == 21:
        printTotal(n)
        print('BLACKJACK!')
        exit()
    elif n > 21:
        printTotal(n)
        print('BUST!')
        exit()
    elif n > 17 and n < 21:
        printTotal(n)
        print('Stay.')
        exit()
    else:
        while n < 21:
            if n < 17:
                printTotal(n)
                print('Hit.')
                randChoice = random.choice(list(cards.keys()))
                randCard = cards[randChoice]
                n += randCard
                print(f'Your newest card has a value of {randChoice}. Your total is now {n}')

                if n > 21:
                    print('BUST')
                    break
                if n == 21:
                    print('BLACKJACK!')
                    break
                else:
                    continue
            elif n == 21:
                printTotal(n)
                print('BLACKJACK!')
                break
            else:
                printTotal(n)
                print('Stay.')
                break

sum = 0

for card in playerCards:

    if playerCards[card] == 'A':
        playerCards[card] = 1

    elif playerCards[card] == 'J' or playerCards[card] == 'Q' or playerCards[card] == 'K':
        playerCards[card] = 10
        
    else:
        playerCards[card] = int(playerCards[card])

    sum += playerCards[card] 

hitStayBust(sum)

