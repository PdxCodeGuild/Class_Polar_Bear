# Notes from the mob coding in class

import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

while True:
    length = input('Enter the number of characters for your password: ')
    try:
        lenth = int(length)
        break
    except ValueError:
        print('Invalid number, try again.')
password = []
while len(password) < length:
    password.append(random.choice(characters))
printable_password = ''.join(password)
print(printable_password)

# for x in range(length):
#     password = password + random.choice(characters)
# print(password)