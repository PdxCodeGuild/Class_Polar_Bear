"""
Ask the user for how many lowercase letters,
uppercase letters, numbers, and special characters they'd
like in their password. You do not want the pieces in order
(e.g. 3 lowercase letters followed by 3 uppercase letters...).
You can use list(password_string) or password_string.split('') to
convert the string to a list, random.shuffle(password_list) to shuffle it,
and then ''.join(password_list) to turn it back into a string.
"""

import random
import string


def verify_int(message):
    while True:
        length = input(message)
        try:
            length = int(length)
            break
        except ValueError:
            print('Invalid number, try again.')
    return length

password = ''

lower_letters = verify_int('Enter number of lowercase letters: ')
for x in range(lower_letters):
    password += random.choice(string.ascii_lowercase)

uppercase_letters = verify_int('Enter number of uppercase letters: ')
for x in range(uppercase_letters):
    password += random.choice(string.ascii_uppercase)

numbers = verify_int('Enter the number of digits: ')
for x in range(numbers):
    password += random.choice(string.digits)

punctuation = verify_int('Enter number of special characters: ')
for x in range(punctuation):
    password += random.choice(string.punctuation)

password_list = list(password)
random.shuffle(password_list)

password = "".join(password_list)

print(password)