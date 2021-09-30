import random

x = random.randint(1,10)

while True:
    user_input = input("Enter a number 1 - 10")
    try:
        user_input = int(user_input)
    except ValueError:
        print("Thats not a valid number")
        
    if user_input != x:
        print("")




