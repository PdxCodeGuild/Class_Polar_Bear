'''
PASSWORD GENERATOR

# Part 1

Let's generate a password of length n using a while loop and random.choice, 
this will be a string of random characters, e.g. a62xB95. 
Allow the user to enter the value of n, remember to convert its type to an int, as input returns a string.
Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.
'''

import random
import string

# start the loop and ask the users how many characters they want their password to be 
while True:

    n = input("Welcome to Random Password Generator, please enter the length for your password (i.e. 10): ")

    try:
        n = int(n)
        break
    except ValueError:
        print("Incorrect entry. Please enter a number.")
        continue

# define our empty string for password
password = ""

# we define our variables of strings so we can pull strings/digits/symbols from here down in our code
letters_lower = string.ascii_lowercase
letters_upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

# start while loop to generate 10 characters long password
while len(password) < n:
    # we generate a random character
    random_character = random.choice(letters_lower + letters_upper + digits + symbols) 
    # we add every random character to the loop/iteration
    password += random_character

# we print the password
print(f"Your password is: {password}")