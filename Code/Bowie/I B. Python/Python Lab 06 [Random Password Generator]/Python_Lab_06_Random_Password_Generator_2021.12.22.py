# ---------------- #
# Python Lab 6 
# Random Password Generator
# 2021.12.22 [updated]
# ---------------- #

# Let's generate a password of length n using a while loop and random.choice, 
# this will be a string of random characters, e.g. a62xB95. Allow the user 
# to enter the value of n, remember to convert its type to an int, 
# as input returns a string. Hint: random.choice can be used to pick 
# a character out of a string, as well as an element out of a list.

import random

source = "abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ0123456789"

def generate_password(n: int):
    password = ""
    while(len(password) < n):
        password += random.choice(source)
    return password

if __name__ == "__main__":
    n = input("Please select a password length / Veuillez choisir une longueur du mot de passe: ")
    while(not n.isdigit()):
        n = input("Please enter an integer value / Veuillez saisir un nombre entier: ")
    print(generate_password(int(n)))

# ---------------- #