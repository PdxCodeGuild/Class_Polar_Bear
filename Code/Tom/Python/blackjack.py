cards={
    'A': 11,
    'A2':1,
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

def add_hand(question):
    while True:
        your_card=input(question)
        if your_card.upper() in cards:
            return your_card.upper()
            break
        else: 
            print(f'{your_card} is not a card, try again.')
            continue

first_card=add_hand('What is your first card?: ')
second_card=add_hand('What is your second card?: ')
third_card=add_hand('What is your third card?: ')
hand=[
    first_card,
    second_card,
    third_card
]

for i in hand:
    hand_value=cards[hand[0]]+cards[hand[1]]+cards[hand[2]]
    if hand_value > 21 and i=='A':
        hand[hand.index(i)]='A2'

if hand_value >= 17 and hand_value < 21:
    advice='Stay.'
elif hand_value < 17:
    advice='Hit.'
elif hand_value == 21:
    advice='Blackjack!'
else:
    advice='Bust!'

print(f'{hand_value} {advice}')