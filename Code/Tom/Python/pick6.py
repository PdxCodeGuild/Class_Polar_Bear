'''
Pick 6
'''

import random

'''Generate Ticket'''
def ticket_gen (ticket=[]):
    ticket=[]
    while len(ticket) < 6:
        ticket.append(random.choice(range(1, 99))) 
    return ticket

'''Calculate matches'''
def ticket_match (win_tick,ticket):
    counter=0
    index_num=0
    for num in win_tick:
        if num == ticket[index_num]:
            counter+=1
            index_num+=1
        else:
            index_num+=1
    return counter

'''Calculate Winnings'''
def win_cal (matches_num):
    winnings=0
    if matches_num==1:
        winnings+=4
    elif matches_num==2:
        winnings+=7
    elif matches_num==3:
        winnings+=100
    elif matches_num==4:
        winnings+=50000
    elif matches_num==5:
        winnings+=1000000
    elif matches_num==6:
        winnings+=25000000
    return winnings

total_winnings=0

'''Function that compares however many tickets to the winning ticket'''
ticket_win=ticket_gen()
def ticket_trys (win_tick, num_try):
    counter=0
    winnings=0
    while counter < num_try:
        ticket=ticket_gen()
        matches=ticket_match(win_tick, ticket)
        winnings+=win_cal(matches)
        counter+=1
    return winnings


total_tries=100000

win=ticket_trys(ticket_win, total_tries)

lose=total_tries*-2

roi=(total_winnings - lose)/lose

print(roi)

total_winnings+=win

print(f'Your total winnings after {total_tries} tries is {total_winnings}.\nYour total loses are {lose}.\nYour ROI is {roi}.')
