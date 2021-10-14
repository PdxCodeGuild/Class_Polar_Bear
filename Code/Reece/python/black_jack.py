# DICTIONARIES #

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

count = 0
number_aces = 0
hand_value = 0
hand = {}

# def aces_check(card_type, aces):
#     if card_type == 'A':
#         aces += 1
#     return aces
# check each card_1, card_2 etc. individual for aces and add to aces from there? #


while count < 3:
    card = input(f'Enter your card value: ').upper()
    if card in cards:
        card_label = f'card_{count}'
        card_name_type = {card_label: card}
        hand.update(card_name_type)
        card_value = cards[hand[card_label]]
        # number_aces += aces_check(card, number_aces)
        if card == 'A':
            number_aces += 1
        # aces_check(hand, card_label, number_aces)
        # print(number_aces)
        # hand_value = aces_check(hand[] + hand[] + hand[])
        count += 1
    else:
        card = input(f'Enter your card value: ').upper()

# print(number_aces)

if number_aces = 1 and hand_value > 21:
    hand_value -= 10
    if hand_value > 21 and number_aces > 1:
        hand_value -= 10

# fix this ^


print(hand_value)
# c = 'A'

# print(aces_check(c, number_aces))

# hand_value = aces_check(hand[] + hand[] + hand[])

# print(cards[hand[0]])

# print(hand_value)
# print(hand)

# hand_value = aces_check(hand[card_0] + hand[card_1] + hand[card_2])


# sum_player_cards = sum(card1_value + card2_value + card3_value)

# if sum_player_cards > 21:
#     print(f'\nSum of your cards is {sum_player_cards}. Advise saying "Already Busted".\n')
# elif sum_player_cards == 21:
#     print(f'\nSum of your cards is {sum_player_cards}. Advise saying "Blackjack".\n')
# elif sum_player_cards < 17:
#     print(f'\nSum of your cards is {sum_player_cards}. Advise saying "Hit me".\n')
# else:
#     print(f'\nSum of your cards is {sum_player_cards}. Advise saying "Stay"\n')