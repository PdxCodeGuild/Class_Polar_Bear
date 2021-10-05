"""
Let's generate a password of length n using a while loop and random.choice, 
this will be a string of random characters, e.g. a62xB95. Allow the user to
enter the value of n, remember to convert its type to an int, as input returns a string.
Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.
"""

import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

while True:
    length = input('Enter the number of characters for your password: ')
    try:
        length = int(length)
        break
    except ValueError:
        print('Invalid number, try again.')

# password = []
# while len(password) < length:
#     password.append(random.choice(characters))

# printable_password = "".join(password)
# print(printable_password)

# password = ""
# for x in range(length):
#     password = password + random.choice(characters)

# print(password)