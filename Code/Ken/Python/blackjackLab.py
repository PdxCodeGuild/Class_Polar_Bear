#Blackjack Advice

card_value = {
    "A":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6, 
    "7":7, 
    "8":8, 
    "9":9, 
    "10":10, 
    "J":10, 
    "Q":10, 
    "K":10
    }

    
card1 = None
while card1 not in card_value:
    card1 = input("What is your first card? >").upper()

card2 = None
while card2 not in card_value:    
    card2 = input("What is your second card? >").upper()

card3 = None
while card3 not in card_value:
    card3 = input("What is your third card? >").upper()



def blackjack():
    total = card_value[card1] + card_value[card2] + card_value[card3]
    if total < 17:
        return print(f"{total} Hit!")
    elif 16 > total > 21:
        return print(f"{total} Stay")
    elif total == 21:
        return print(f"{total} Blackjack!")
    elif total > 21:
        return print(f"{total} Busted!")
        
blackjack()

#def ace_check(hand):
     # hand is a list of cards in players hand
     #if 'A' in hand:
