# Reece Adams - lab 04 in class - lab 8 - Pick 6 #
import random

# Generate a list of 6 random numbers representing the winning tickets
def pick6():
    ticket = []
    for i in range(6):
        ticket_number = random.randint(1, 99)
        ticket.append(ticket_number)
    return ticket

# Start your balance at 0
balance = 0

# for each loop Generate a list of 6 random numbers representing the ticket
run_length = int(input('Enter the number of tickets you would like to purchase: '))
def game_tickets():
    ticket_dictionary = {}
    for i in range(run_length):
        game_ticket = pick6()
        ticket_dictionary.update({i : game_ticket})
    return ticket_dictionary

# Subtract 2 from your balance (you bought a ticket)
spent = 0
spent += run_length * 2

# Find how many numbers match
def match_check(winning, ticket):
    number_matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            number_matches += 1
    return number_matches

# Add to your balance the winnings from your matches
winning_amounts = {
    0:0,
    1:4,
    2:7,
    3:100,
    4:50000,
    5:1000000,
    6:25000000
}
def add_winnings():
    winnings = 0
    matches = 0
    winning_ticket = pick6()
    for i in range(run_length):
        game_ticket = pick6()
        matches = match_check(winning_ticket, game_ticket)
        winning_amounts[matches]
        winnings += winning_amounts[matches]
    return winnings
winnings = add_winnings()
balance = balance - spent + winnings
# print(balance)

# After the loop, print the final balance
ROI = (winnings - spent)/ spent
print(f'\nYour final balance is {balance}. The ROI was {ROI}.\n')