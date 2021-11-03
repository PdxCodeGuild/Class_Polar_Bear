# define Cards





cards  = {
    'A' : 1,
     '2' : 2,
     '3' : 3,
     '4' : 4,
     '5' : 5,
     '6' : 6,
     '7' : 7,
     '8' : 8,
     '9' : 9,
     '10' : 10,
     'J' : 10,
     'Q' : 10,
     'K' : 10
}

#ask for 3 cards
def ace_check(hand):
    # hand if a list
    
    score = cards[hand[0]] + cards[hand[1]] + cards[hand[2]]
    if score > 21 and 'A' in hand:
        score -= 10
    if score > 21 and 'A' in hand:
        score -= 10
    return score



first_card = None
while first_card not in cards:
    first_card = input('Whats your first card? ').upper()

second_card = None
while second_card not in cards:
    second_card = input('Whats your second card? ').upper()

third_card = None
while third_card not in cards:
    third_card = input('Whats your third card? ').upper()


# determine value of hand
sum_of_score = ace_check([first_card, second_card, third_card])


# give advice
if sum < 17 :
    print('hit')
elif sum >= 17 and sum < 21:
    print('stay')
elif sum_of_score == 21:
    print('Blackjack!')
else:
    print('bust')

