# DICTIONARIES #

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
    'K': 10
}

'''while True:
    card1 = input('Enter your 1st card: ')
    card2 = input('Enter your 2nd card: ')
    card3 = input('Enter your 3rd card: ')
    for key in cards:
        if key == card1:
            card1_value = cards[key]
        if key == card2:
            card2_value = cards[key]
        if key == card3:
            card3_value = cards[key]
    sum_player_cards = (card1_value + card2_value + card3_value)
    if sum_player_cards > 21:
        print(f'\nSum of your cards is {sum_player_cards}. Advise saying "Already Busted".')
        break
    elif sum_player_cards == 21:
        print(f'\nSum of your cards is {sum_player_cards}. Advise saying "Blackjack".')
        break
    elif sum_player_cards < 17:
        print(f'\nSum of your cards is {sum_player_cards}. Advise saying "Hit me".')
        break
    else:
        print(f'\nSum of your cards is {sum_player_cards}. Advise saying "Stay"')
        break'''

# FUNCTION PRACTICE...NOT EFFICIENT AT ALL 

card1 = ''
card1_value = []
card2 = ''
card2_value = []
card3 = ''
card3_value = []

def cardinput(card, card_value):
    card = input(f'Enter your card value: ')
    while True:
        # card = input(f'Enter your card value: ')
        try:
            card = card.upper()
            break
        except:
            try:
                card = int(card)
                break
            except ValueError:
                card = input(f'Inavlid card Value...Please enter your value: ')
                break
    for key in cards:
        if key == card:
            card_value = card_value.append(cards[key])
    # print(card, card_value)
    return card, card_value

cardinput(card1, card1_value)
cardinput(card2, card2_value)
cardinput(card3, card3_value)

sum_player_cards = sum(card1_value + card2_value + card3_value)

if sum_player_cards > 21:
    print(f'\nSum of your cards is {sum_player_cards}. Advise saying "Already Busted".\n')
elif sum_player_cards == 21:
    print(f'\nSum of your cards is {sum_player_cards}. Advise saying "Blackjack".\n')
elif sum_player_cards < 17:
    print(f'\nSum of your cards is {sum_player_cards}. Advise saying "Hit me".\n')
else:
    print(f'\nSum of your cards is {sum_player_cards}. Advise saying "Stay"\n')