import random


def init():
    total = 0
    expenses = 0
    loop_itiration = 100000
    ticket_cost = 2
    ROI = 0

    for _ in range(loop_itiration):
        winning_numbers = pick6()
        ticket_numers = pick6()
        total_match = num_matches(
            winning=winning_numbers, ticket=ticket_numers)
        winning_amount = payout(total_match)
        total += winning_amount
        expenses += ticket_cost
        # print(winning_numbers, ticket_numers)
        # winning = [1, 2, 4, 5, 6]
        # ticket = [1, 2, 3, 5, 6]
        # total_match = num_matches(winning, ticket)
        # winning_amount = payout(total_match)
    earnings = total - expenses

    if (earnings < 0):
        m = '{:,.2f}'.format(int(abs(earnings)))
        print(f"You're down ${m}")
    else:
        print(f"You have won a total of {earnings}")
    ROI = (earnings - expenses)/expenses * 100
    print(f"Your total ROI is {round(ROI)}%")


def pick6():
    random_six = []
    for _ in range(6):
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
