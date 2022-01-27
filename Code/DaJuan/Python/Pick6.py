from math import exp
import random
# Generate a list of 6 random numbers representing the winning tickets
def pick6():
    ticket = []
    for i in range(6):
        number = random.randint(1,99)
        ticket.append(number)

    return ticket

def matches(winning, ticket):
    # [89, 88, 75, 34, 20, 19]
    # [90, 88, 4, 34, 99, 19]
    num_matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            num_matches += 1

    return num_matches


prize_pool = {
    1: 4,
    2: 7,
    3: 100,
    4: 50_000,
    5: 1_000_000,
    6: 25_000_000
}


# Start your balance at 0
expenses = 0
earnings = 0
winning = pick6()

# Loop 100,000 times, for each loop:
count = 0
while count < 100_000:
    count += 1

    # Generate a list of 6 random numbers representing the ticket
    ticket = pick6()

    # Subtract 2 from your balance (you bought a ticket)
    expenses += 2

    # Find how many numbers match
    num_matches = matches(winning, ticket)

    # Add to your balance the winnings from your matches
    earnings += prize_pool.get(num_matches, 0)
    


# After the loop, print the final balance
print(f"${earnings - expenses}")
print(f"ROI: {(earnings - expenses) / expenses}")