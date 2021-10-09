# Reece Adams - lab08.py - Pick6 #

import random

# 1ST PART = Generate a list of 6 random numbers representing the winning tickets #

# pick6_list = []

# def ran_tick():
#     pick6_list = []
#     for i in range(6): #may be useful comparing winner i position to play i position
#         pick6_list.append(random.randint(1,99))
#     return pick6_list

# winning_list = [1,2,3,4,5,6] #ran_tick()

# player_list = [1,2,3,4,5,0]# ran_num()

# 2ND PART Start your balance at 0 #

# balance = 0

# 3RD PART Loop 100,000 times, for each loop: #

# def game_loop():
#     repititions = 0
#     for i in range(100000):
#         repititions += 1
#     return repititions

# 4TH PART Generate a list of 6 random numbers representing the ticket #

# def list_check(list1, list2=winning_list): # add in calculations within this function
#     matches = 0
#     for i in range(1):
#         if list1[i] == list2[i]:
#             matches += 1
#     return matches # add in calculations within this function here to return earning with a variable

# def game_loop():
#     matches = 0
#     balance = 0
#     repititions = 0
#     for i in range(100000):
#         repititions += 1
#         player_ticket = ran_tick()
#     return repititions


# 5TH PART Subtract 2 from your balance (you bought a ticket)

# def purchases(num_purc):
#     num_purc -= 2

# def game_loop():
#     matches = 0
#     balance = 0
#     repititions = 0
#     for i in range(100000):
#         repititions += 1
#         player_ticket = ran_tick()
#         purchases(repititions)
#     return repititions, balance

# print(game_loop())

# 6TH PART Find how many numbers match #

balance = 0
num_tickets = 100000
winning_list = [1,2,3,4,5,6] #rant_tick() # fine to be here right now, but later needs to go below function ran_tick definition
pick6_list = [1,2,3,4,5,6]

def ran_tick():
    pick6_list = []
    for i in range(6): #may be useful comparing winner i position to play i position
        pick6_list.append(random.randint(1,99))
    return pick6_list

def list_check(list1, list2=winning_list): # add in calculations within this function
    matches = 0
    for i in range(1):
        if list1[i] == list2[i]:
            matches += 1
    return matches 

def purchases(num_purc):
    num_purc -= 2

matches = 1
def earnings(matches):
    tick_earnings = 0
    if matches == 1:
        tick_earnings += 4
    elif matches == 2:
        tick_earnings += 7
    elif matches == 3:
        tick_earnings += 100
    elif matches == 4:
        tick_earnings +=50000
    elif matches == 5:
        tick_earnings += 1000000
    elif matches == 6:
        tick_earnings += 25000000
    else:
        tick_earnings = 0
    # print(tick_earnings)
    return tick_earnings

# matches = 1
earnings(matches)
print(tick_earnings)

# print(earnings(matches))

def list_check(list1): # add in calculations within this function
    matches = 0
    winning_list = [1,2,3,4,5,6]
    for i in range(6):
        if list1[i] == winning_list[i]:
            matches += 1
            # earnings()
            # print(earnings)
        else:
            matches = 0
    earnings(matches)
    return matches, # add in calculations within this function here to return earning with a variable

# list_check(pick6_list)

def game_loop():
    repititions = 0
    for i in range(num_tickets):
        repititions += 1
        player_ticket = [1,2,3,4,5,6]# ran_tick()
        list_check(player_ticket)
        purchases(repititions)
    print(earnings)
    return repititions, matches, earnings

# 7TH PART Add to your balance the winnings from your matches #

# game_loop()

# print(earnings)

# balance += num_tickets * -2

# final_balance = balance + earnings

# 8TH PART After the loop, print the final balance #

# print(final_balance)