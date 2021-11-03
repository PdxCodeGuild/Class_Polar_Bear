# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:


from string import capwords


deck_of_cards = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
hand = []
def verify_card(message):
    while True:
        card = input(message)
        key = card.upper() 
        if key in deck_of_cards:
            #print('That is a valid card.')
            break
        else:
            print('this is not a valid card.')
            continue
    return key



print('Use one character or number to describe your card: ')
first_card = verify_card("What's your first card: ")
second_card = verify_card("What's your second card: ")
third_card = verify_card("What's your third card: ")

hand_value = []
if first_card in deck_of_cards:
    hand_value.append(deck_of_cards[first_card])
if second_card in deck_of_cards:
    hand_value.append(deck_of_cards[second_card])
if third_card in deck_of_cards:
    hand_value.append(deck_of_cards[third_card])
    # for card in deck_of_cards:
    #         hand_value.append(deck_of_cards[first_card])
    # print(f'{deck_of_cards[first_card]}')
    # card_value = ({deck_of_cards[first_card]})
    # # card_value = int(card_value)
    # hand.append(card_value)

# if second_card in deck_of_cards:
#     print(f'{deck_of_cards[second_card]}')
#     hand.append({deck_of_cards[second_card]})
# if third_card in deck_of_cards:
#     print(f'{deck_of_cards[third_card]}')
#     hand.append({deck_of_cards[third_card]})

total = sum(hand_value)
print(f'Total points in your had: {total}')

if total < 17:
    print('You should hit.')
elif total >= 17 and total < 21:
    print('You should stay')
elif total == 21:
    print('Blackjack!')
elif total > 21:
    print('You already busted.')

# total = sum(hand)
# print(total)
# • Less than 17, advise to "Hit"
# • Greater than or equal to 17, but less than 21, advise to "Stay"
# • Exactly 21, advise "Blackjack!"
# • Over 21, advise "Already Busted"
# Print out the current total point value and the advice.