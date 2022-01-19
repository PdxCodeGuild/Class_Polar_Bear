# ---------------- #
# BlackJack
# ---------------- #

# Blackjack Advice

# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards.
# First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
# Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. 
# At this point, assume aces are worth 1. Use the following rules to determine the advice:

# * Less than 17, advise to "Hit"
# * Greater than or equal to 17, but less than 21, advise to "Stay"
# * Exactly 21, advise "Blackjack!"
# * Over 21, advise "Already Busted"

# Print out the current total point value and the advice.

# ```
# What's your first card? Q
# What's your second card? 2
# What's your third card? 3
# 15 Hit

# What's your first card? K
# What's your second card? 5
# What's your third card? 5
# 20 Stay

# What's your first card? Q
# What's your second card? J
# What's your third card? A
# 21 Blackjack!
# --------------- #

# 2, 3, 4, 5, 6, 7, 8, 9
# 10, J, Q, K
# A

# create dictionary

cardValue = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
'J': 10, 'Q': 10, 'K': 10, 'A': 1}

# code to store values of the user

value1 = input("What is your first card?: ")
value2 = input("What is your second card?: ")
value3 = input("What is your third card?: ")

def cardInitialCardSum():
    return  cardValue[value1] + cardValue[value2] + cardValue[value3]


# analyze values from the user and give advice

# * Less than 17, advise to "Hit"
# * Greater than or equal to 17, but less than 21, advise to "Stay"
# * Exactly 21, advise "Blackjack!"
# * Over 21, advise "Already Busted"

if cardInitialCardSum() < 17:
    print(cardInitialCardSum(), 'Hit')

if cardInitialCardSum() >= 17 and cardInitialCardSum < 21:
    print(cardInitialCardSum(),'stay')

if cardInitialCardSum() == 21:
    print(cardInitialCardSum(),'BlackJack!')

if cardInitialCardSum() > 21:
    print(cardInitialCardSum(),'Already busted!')

# 21 Blackjack!