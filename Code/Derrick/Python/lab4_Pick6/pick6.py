import random 

def pick_numbers():
    final_list = []
    for i in range(6):
        final_list.append(random.randint(1,6))
    return final_list  

def winning_numbers():
    
    winning_numbers = pick_numbers()

    return winning_numbers

def ticket(num_of_tickets):
    balance = 0
    expenses = 0
    earnings = 0
    for i in range(num_of_tickets):
        user_numbers = pick_numbers()
        balance -= 2
        expenses += 2
        matches = 0
        for i in range(6):
            if user_numbers[i] == x[i]:
                matches += 1

        if matches == 1:
            balance += 4
        elif matches == 2:
            balance += 7
        elif matches == 3:
            balance += 100
        elif matches == 4:
            balance += 50000
        elif matches == 5:
            balance += 1000000
        elif matches == 6:
            balance += 25000000
        else:
            balance += 0
            earnings += 0

    print(balance)
    


    
x = winning_numbers()
print(x)
ticket(5)

