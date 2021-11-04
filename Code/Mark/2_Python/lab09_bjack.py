def calc(card):
    try:
        return int(card)
    except ValueError:
        if card == 'A':
            return 1
        if card in {'J', 'Q', 'K'}:
            return 10
        print(f'{card} is not a valid card.')
        exit()

c1 = input('What\'s your first card?  ')
c2 = input('What\'s your second card? ')
c3 = input('What\'s your third card?  ')

points = calc(c1) + calc(c2) + calc(c3)
if points < 17:
    print(f'{points} Hit')
elif points < 21:
    print(f'{points} Stay')
elif points > 21:
    print(f'{points} Busted')
else:
    print(f'{points} Blackjack!')

