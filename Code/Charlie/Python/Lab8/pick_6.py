import random

    # Generate a list of 6 random numbers representing the winning tickets

def winning():
    win_list = []
    for i in range(6):
        win_list.append(random.randint(1,99))
    return win_list
       
    # Generate a list of 6 random numbers representing the ticket
def matches(winning, win_list):
    matches = 0
    for i in range(len(win_list)):
        if winning[i] == win_list[i]:
            matches += 1
    return matches

    # Start your balance at 0
def play():
    win = winning()
    balance = 0
    earnings = 0
    winnings = []



    # Loop 100,000 times, for each loop:
    # Subtract 2 from your balance (you bought a ticket)
    # Find how many numbers match
    # Add to your balance the winnings from your matches
    # After the loop, print the final balance

