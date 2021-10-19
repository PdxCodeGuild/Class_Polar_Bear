# Reece Adams - Lab9.py - Blackjack Advice

# Version 1

# cards = {
#     'A': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9,
#     '10': 10,
#     'J': 10,
#     'Q': 10,
#     'K': 10
# }

# card1 = ''
# card1_value = []
# card2 = ''
# card2_value = []
# card3 = ''
# card3_value = []

# def cardinput(card, card_value):
#     card = input(f'Enter your card value: ')
#     while True:
#         # card = input(f'Enter your card value: ')
#         try:
#             card = card.upper()
#             break
#         except:
#             try:
#                 card = int(card)
#                 break
#             except ValueError:
#                 card = input(f'Inavlid card Value...Please enter your value: ')
#                 break
#     for key in cards:
#         if key == card:
#             card_value = card_value.append(cards[key])
#     # print(card, card_value)
#     return card, card_value

# cardinput(card1, card1_value)
# cardinput(card2, card2_value)
# cardinput(card3, card3_value)

# sum_player_cards = sum(card1_value + card2_value + card3_value)

# if sum_player_cards > 21:
#     print(f'\nSum of your cards is {sum_player_cards}. Advise saying "Already Busted".\n')
# elif sum_player_cards == 21:
#     print(f'\nSum of your cards is {sum_player_cards}. Advise saying "Blackjack".\n')
# elif sum_player_cards < 17:
#     print(f'\nSum of your cards is {sum_player_cards}. Advise saying "Hit me".\n')
# else:
#     print(f'\nSum of your cards is {sum_player_cards}. Advise saying "Stay"\n')

# Version 2

playing_cards = {
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

card_list = []
card_count = 0
aces = 0
hand = 0

def ace_count(list, aces):
    for i in list:
        if i == 'A':
            aces += 1
    return aces

def hand_sum(hand):
    for i in card_list:
        if i in playing_cards:
            hand += playing_cards[i]
    return hand

def value_corection(hand, aces):
    if hand > 21 and aces > 0:
        hand -= 10
        aces -= 1
        if hand > 21 and aces > 0:
            hand -=10
    return hand

while card_count <3:
    card = input('Enter your card: ')
    card_list.append(card)
    card_count += 1
    number_aces = ace_count(card_list, aces)
hand_value = hand_sum(hand)
hand_value = value_corection(hand_value, number_aces)

if hand_value > 21:
    print(f'\nSum of your cards is {hand}. Advise saying "Already Busted".\n')
elif hand_value == 21:
    print(f'\nSum of your cards is {hand_value}. Advise saying "Blackjack".\n')
elif hand_value < 17:
    print(f'\nSum of your cards is {hand_value}. Advise saying "Hit me".\n')
else:
    print(f'\nSum of your cards is {hand_value}. Advise saying "Stay"\n')