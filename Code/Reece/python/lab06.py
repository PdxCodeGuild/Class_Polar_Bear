# Reece Adams - lab06.py - lab 6 - Random Password Generator #

import random
import string


#  PART 2 -------------------------------------------------------------------------------------------- #


# VARIABLES #
digits = string.digits
punct = string.punctuation
low_let = string.ascii_lowercase
upp_let = string.ascii_uppercase
chars = digits + punct + low_let + upp_let
password = []
p_digits = []
p_punct = []
p_low = []
p_upp = []

# DIGITS LENGTH, CHECK, AND WHILE LOOP #

n_digits = input('Enter the number of DIGITS you would like in your password: ')

try:
    n_digits = int(n_digits)
except ValueError:
    print("Invalid number, please try again.")
    n_digits = input('Enter the number of DIGITS you would like in your password: ')
n_digits = int(n_digits)

while len(p_digits) < n_digits:
    p_digits.append(random.choice(digits))

# SPECIAL CHARACTERS LENGTH, CHECK, AND WHILE LOOP #

n_punct = input('Enter the number of SPECIAL CHARACTERS you would like in your password: ')

try:
    n_punct = int(n_punct)
except ValueError:
    print("Invalid number, please try again.")
    n_punct = input('Enter the number of SPECIAL CHARACTERS you would like in your password: ')
n_punct = int(n_punct)

while len(p_punct) < n_punct:
    p_punct.append(random.choice(punct))

# LOWERCASE LETTERS LENGTH, CHECK, AND WHILE LOOP #

n_low = input('Enter the number of LOWERCASE LETTERS you would like in your password: ')

try:
    n_low = int(n_low)
except ValueError:
    print("Invalid number, please try again.")
    n_low = input('Enter the number of LOWERCASE LETTERS you would like your password to be: ')
n_low = int(n_low)

while len(p_low) < n_low:
    p_low.append(random.choice(low_let))

# UPPERCASE LETTERS LENGTH, CHECK, AND WHILE LOOP #

n_upp = input('Enter the number of UPPERCASE LETTERS you would like in your password: ')

try:
    n_upp = int(n_upp)
except ValueError:
    print("Invalid number, please try again.")
    n_upp = input('Enter the number of UPPERCASE LETTERS you would like in your password: ')
n_upp = int(n_upp)

while len(p_upp) < n_upp:
    p_upp.append(random.choice(upp_let))

# COMBINING ALL CHARACTERS INTO A PASSWORD #

password = (p_digits + p_punct + p_low + p_upp)
random.shuffle(password)
password = ''.join(password)

# PRINT PASSWORD #

print(f'\nYour randomly generated password is:\n{password}\n')

#  PART 1 -------------------------------------------------------------------------------------------- #

# # VARIABLES #
# digits = string.digits
# punct = string.punctuation
# low_let = string.ascii_lowercase
# high_let = string.ascii_uppercase
# chars = digits + punct + low_let + high_let
# password = []
# prnt_password = (''.join(map(str, password)))

# # PASSWORD LENGTH #

# n = input('Enter the number of characters you would like youwer

# try:
#     n = int(n)
# except ValueError:
#     print("invalid number try again")
#     n = input('Enter the number of characters you would like your password to be: ')
# n = int(n)

# # WHILE LOOP #

# while len(password) < n:
#     password.append(random.choice(chars))

# # PRINT PASSWORD #

# prnt_password = (''.join(map(str, password)))
# print(f'\nYour randomly generated password is:\n{prnt_password}\n')