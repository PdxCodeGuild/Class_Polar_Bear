# Define card values
cards = {
    'A': 11,
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
    'K': 10
}

def ace_check(hand):
    # hand is a list ex: ['A', '5', '4']
    # ['10', 'A', 'A'] 31
    score = cards[hand[0]] + cards[hand[1]] + cards[hand[2]]
    if score > 21 and 'A' in hand:
        score -= 10
        if score > 21:
            score -= 10

    # while 'A' in hand and score > 21:
    #     score -= 10
    #     hand.remove('A')

    return score
    

print(f'Available cards: {cards.keys()}')
# Ask player for 3 cards
first_card = None
while first_card not in cards:
    first_card = input('Enter your first card: ').upper()

second_card = None
while second_card not in cards:
    second_card = input('Enter your second card: ').upper()

third_card = None
while third_card not in cards:
    third_card = input('Enter your third card: ').upper()

# Determine value of hand
sum_of_score = ace_check([first_card, second_card, third_card])

# Give player advice based on hand score
if sum_of_score < 17:
    print(f'{sum_of_score} Hit!')
elif sum_of_score >= 17 and sum_of_score < 21:
    print(f'{sum_of_score} Stay.')
elif sum_of_score == 21:
    print(f'{sum_of_score} Blackjack!!!')
else:
    print(f'{sum_of_score} Sorry, you busted....')