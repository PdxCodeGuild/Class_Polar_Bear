import random
import math
# from typing_extensions import TypeVarTuple

winning_numbers = []
my_ticket = []
pick_winning_numbers = [1, 2, 3, 4, 5, 6]
check_winning_numbers = [1, 2, 3, 4, 5, 6]
pick_6_number = range(1, 99)
money_won = []
number_matches = 0
total_money_won = 0
money_paid = []
roi = float

def pick6():
    pick6_ticket = []
    for numbers in pick_winning_numbers:
        pick6_ticket.append(random.choice(pick_6_number))
    return pick6_ticket
        # print(f' counting number: {numbers}\n')
        # winning_numbers.append(random.choice(pick_6_number))
        # # print(f' winning numbers: {winning_numbers[numbers]}')
        # my_ticket.append(random.choice(pick_6_number))

    # print(f' my  number: {my_ticket[numbers]}\n')
def number_matches(winning, ticket):
    matched = 0
    if winning == ticket:
        matched += 1
    return matched


    # for numbers in check_winning_numbers:
    #     winning = winning_numbers[numbers]
    #     ticket = my_ticket[numbers]
    #     if winning_numbers[numbers] == my_ticket[numbers]:
    #         # print(f'This is the position that won {numbers}')
    #         # print(f'my ticket {my_ticket[numbers]}')
    #         # print(f'winning number: {winning_numbers[numbers]}')
    #         # print(f'numbered matched {number_matches}')
    # return number_matches

purchased_tickets = 0
tickets = 100000

winning_numbers = pick6()
#winning_numbers = pick6()
print(f'\nwinning numbers {winning_numbers}\n')
while purchased_tickets < tickets:
    purchased_tickets += 1
    total_good_numbers = 0
    my_ticket = pick6()
    for numbers in check_winning_numbers:
        numbers = numbers - 1
        good_number = number_matches(winning_numbers[numbers], my_ticket[numbers])
        # print(f'w: {winning_numbers[numbers]}')
        # print(f't: {my_ticket[numbers]}')
        # print(f'good: {good_number}')
        total_good_numbers = total_good_numbers + good_number
    # print(f'my ticket: {my_ticket}')
    # print(f'winning numbers {winning_numbers}')
    # print(f'total per ticket: {total_good_numbers}')
    # This is where you pay for each ticket
    money_paid.append(2)
    # This is where you get paid for each winning number
    if total_good_numbers == 1:
        money_won.append(4)
    elif total_good_numbers == 2:
        money_won.append(7)
    elif total_good_numbers == 3:
        money_won.append(100)
    elif total_good_numbers == 4:
        money_won.append(50000)
    elif total_good_numbers == 5:
        money_won.append(1000000)
    elif total_good_numbers == 6:
        money_won.append(25000000)
print(purchased_tickets)
print(sum(money_won))
print(sum(money_paid))

total_money_won =  sum(money_won) - sum(money_paid)
roi = total_money_won / sum(money_paid)
print(f'your earnings are ${sum(money_won)} \nand your expenses are -${sum(money_paid)} \nwhich leaves you with {total_money_won} \n and an ROI of ${roi}')

# print(f'this should be number of matches {matched}')    

# print(f'winning numbers: {winning_numbers}')




#    return 
# print(f'\nwinning numbers are \n{winning_numbers} \nyour numbers were \n{my_ticket}\n\n\n')


# def pick_winning_numbers(pick_6_number):
#     pick_6_number = random.choice(pick_6_number)
#     # for numbers in winning_numbers:
#     #     print(numbers)
#     # return numbers
#     return pick_winning_numbers

# print(pick_winning_numbers)

