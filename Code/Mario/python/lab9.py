
def one_or_eleven(card, total):
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


def start_game():
    cards = {
        "a": [1, 11]
    }
    for num in range(1, 11):
        cards[str(num)] = num
    total = 0
    print(cards)

    options = ["first", "second", "third"]
    user_cards = []
    play_again = True

    for option in range(len(options)):
        try:
            user_input = input(f"What is your {options[option]} card?").lower()
            if user_input in cards.keys():
                if user_input == 'a':
                    total += one_or_eleven(cards[user_input], total)
                elif user_input == 'j' or user_input == 'q' or user_input == 'k':
                    user_input = "10"
                else:
                    total += (cards[user_input])
                    user_cards.append(cards[user_input])
        except:
            user_cards.append(cards[user_input])
    advise = hints(total)
    print(f"{total} {advise}")


start_game()
