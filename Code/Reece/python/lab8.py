# Reece Adams - lab08.py - Pick6 #

import random

# 1ST PART = Generate a list of 6 random numbers representing the winning tickets #

pick6_list = []

def ran_tick():
    pick6_list = []
    for i in range(6): #may be useful comparing winner i position to play i position
        pick6_list.append(random.randint(1,99))
    return pick6_list

winning_list = [1,2,3,4,5,6] #ran_tick()

# player_list = [1,2,3,4,5,0]# ran_num()

# 2ND PART Start your balance at 0 #

balance = 0

# 3RD PART Loop 100,000 times, for each loop: #

# def game_loop():
#     repititions = 0
#     for i in range(100000):
#         repititions += 1
#     return repititions

# 4TH PART Generate a list of 6 random numbers representing the ticket #

def list_check(list1, list2=winning_list): # add in calculations within this function
    matches = 0
    for i in range(1):
        if list1[i] == list2[i]:
            matches += 1
    return matches # add in calculations within this function here to return earning with a variable

# def game_loop():
#     matches = 0
#     balance = 0
#     repititions = 0
#     for i in range(100000):
#         repititions += 1
#         player_ticket = ran_tick()
#     return repititions


# 5TH PART Subtract 2 from your balance (you bought a ticket)

def purchases(num_purc):
    num_purc -= 2

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

matches = 0
def earnings():
    earnings = 0
    if matches == 1:
        earnings += 4
    elif matches == 2:
        earnings += 7
    elif matches == 3:
        earnings += 100
    elif matches == 4:
        earnings +=50000
    elif matches == 5:
        earnings += 1000000
    elif matches == 6:
        earnings += 25000000
    return earnings


# def game_loop():
#     repititions = 0
#     for i in range(100000):
#         repititions += 1
#     return repititions

def list_check(list1): # add in calculations within this function
    matches = 0
    winning_list = [1,2,3,4,5,6]
    for i in range(6):
        if list1[i] == winning_list:
            matches += 1
        else:
            matches = 0
    return matches # add in calculations within this function here to return earning with a variable

def game_loop():
    # matches = 0
    
    balance = 0
    repititions = 0
    for i in range(100000):
        # matches = 0
        repititions += 1
        player_ticket = [1,2,3,4,5,6]# ran_tick()
        list_check(player_ticket) # MATCH WON'T HAPPEN...BECAUSE IT'S NOT UPDATING IN THE GAME LOOP...DOUBLE GAME LOOP???????!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        purchases(repititions)
    return repititions, balance, matches

player_ticket = [1,2,3,4,5,6]


print(list_check(player_ticket))

    # def game_loop():
    #     repititions = 0
    #     for i in range(100000):
    #         repititions += 1
    #         player_ticket = ran_tick()
    #         list_check(player_ticket) # produuces MATCHES of matching ticket numbers
    #     return repititions, balance

# 7TH PART Add to your balance the winnings from your matches #

# def game_loop():
#     earnings = 0
#     balance = 0
#     repititions = 0
#     for i in range(100000):
#         repititions += 1
#         player_ticket = ran_tick()
#         purchases(repititions)
#         list_check(player_ticket)
#         earnings()
#     return repititions, balance, earnings

# print(game_loop())

# def game_loop():
#     repititions = 0
#     for i in range(100000):
#         repititions += 1
#         player_ticket = ran_tick()
#         list_check(player_ticket) # produuces MATCHES of matching ticket numbers
#         earnings()
#     return repititions


# matches = 0
# def earnings():
#     earnings = 0
#     if matches == 1:
#         earnings += 4
#     elif matches == 2:
#         earnings += 7
#     elif matches == 3:
#         earnings += 100
#     elif matches == 4:
#         earnings +=50000
#     elif matches == 5:
#         earnings += 1000000
#     elif matches == 6:
#         earnings += 25000000
#     return earnings

# # print(earnings())

def list_check(list1, list2=winning_list): # add in calculations within this function
    matches = 0
    for i in range(6):
        if list1[i] == list2[i]:
            matches += 1
    return matches # add in calculations within this function here to return earning with a variable

# check = list_check(player_list)

# print(check)