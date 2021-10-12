import random

def pick6():
    ticket = []
    for i in range(6):
        number = random.randint(1,99)
        ticket.append(number)
    return ticket
# print(pick6())

def matches(winning, ticket):
    num_matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            num_matches += 1
    return num_matches
            
prize_pool={
    1:4,
    2:2,
    3:100,
    4: 50_000,
    5: 1_000_000,
    6: 250_000_000
}

balance = 0 
winning = pick6()
count = 0

while count < 100000:
    count += 1
    ticket = pick6()
    balance -= 2
    num_matches = matches(winning, ticket)
    balance += prize_pool.get(num_matches, 0)
    
print(f"${balance}")