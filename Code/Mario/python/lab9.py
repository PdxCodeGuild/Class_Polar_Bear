
def one_or_eleven(card):
    if total + 11 > 21 and type(card) == list:
        return 1
    elif total + 11 <= 21 and type(card) == list:
        return 11
    else:
        return card


def hints(total):
    if total < 17:
        return 'Hit'
    elif total >= 17 and total < 21:
        return 'Stay'
    elif total == 21:
        return "Blackjack!!!"
    else:
        return "Already Busted"


cards = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "a": [1, 11]
}

total = 0

options = ["first", "second", "third"]
user_cards = []
play_again = True

for option in range(len(options)):
    try:
        user_input = input(f"What is your {options[option]} card?").lower()
        if user_input == 'j' or user_input == 'q' or user_input == 'k':
            user_input = "10"
        if user_input in cards.keys():
            if user_input == 'a':
                total += one_or_eleven(cards[user_input])
            else:
                total += (cards[user_input])
                user_cards.append(cards[user_input])
    except:
        user_cards.append(cards[user_input])
advise = hints(total)
print(f"{total} {advise}")
