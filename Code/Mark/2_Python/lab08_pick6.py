import random

def ticket(t):
    for i in range(6):
        t[i] = random.randint(1,99)

def match(a, b):
    m = 0
    for i in range(6):
        if a[i] == b[i]:
            m += 1
    if m == 1:
        return 4
    if m == 2:
        return 7
    if m == 3:
        return 100
    if m == 4:
        return 50000
    if m == 5:
        return 1000000
    if m == 6:
        return 25000000
    return 0

balance = 0
t, w = 6*[0], 6*[0]
ticket(w)

for i in range(100000):
    ticket(t)
    balance += match(t, w) - 2

print(balance)
