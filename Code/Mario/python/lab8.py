import random


def init():
    total = 0

    for _ in range(100000):
        winning_numbers = pick6()
        ticket_numers = pick6()
        total_match = num_matches(
            winning=winning_numbers, ticket=ticket_numers)
        winning_amount = payout(total_match)
        total += winning_amount - 2

    if (total < 0):
        total = '{:,.2f}'.format(int(abs(total)))
        print(total)
        print(f"You're down ${total}")
    else:
        print(f"You have won a total of {abs(total)}")
        print(abs(-10))


def pick6():
    random_six = []
    for num in range(6):
        random_six.append(random.randint(1, 99))
    return random_six


def num_matches(winning, ticket):
    total_matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            total_matches += 1
    return total_matches


def payout(total_match):
    prize = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000
    }
    return prize[total_match]


init()
