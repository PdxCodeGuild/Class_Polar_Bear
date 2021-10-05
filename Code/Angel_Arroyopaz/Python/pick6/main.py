'''

'''

import random
import math

# function to generate our winning ticket
def random_ticket():
    return(random.sample(range(1, 99), 6))

# function to compare the winning ticket and the users tickets 
# and return the number of matches
def compare(list1, list2):
    matches = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            matches += 1
    
    return matches




# function to determine how much money the user gets 
# depending on the number of matches
def profit(matches, payout=0):
    if matches == 1:
        payout = 4
    elif matches == 2:
        payout = 7
    elif matches == 3:
        payout = 100
    elif matches == 4:
        payout = 50000
    elif matches == 5:
        payout = 1000000
    elif matches == 6:
        payout = 25000000

    return payout

balance = 0
expenses = 0
earnings = 0
winner_ticket = random_ticket()

# loop 100,000 times
for i in range(100000):
    user_ticket = random_ticket()
    expenses += 2
    compare_results = compare(winner_ticket, user_ticket)
    earnings += profit(compare_results)

roi = (earnings - expenses)/expenses
balance = earnings - expenses

print(f"Balance: ${balance}")
print(f"ROI:{roi}%")
print(f"Earnings: ${earnings}")
print(f"Expenses: ${expenses}")

