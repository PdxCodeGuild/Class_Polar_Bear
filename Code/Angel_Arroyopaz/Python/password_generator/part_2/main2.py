'''
PASSWORD GENERATOR


# Part 2 (optional)

Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters
they'd like in their password. You do not want the pieces in 
order (e.g. 3 lowercase letters followed by 3 uppercase letters...). 
You can use list(password_string) or password_string.split('') to convert 
the string to a list, random.shuffle(password_list) to shuffle it, and 
then ''.join(password_list) to turn it back into a string.
'''
#import modules
import random
import string


# we welcome the users and explain whats comming next
# ask the users how many letters, numbers, and symbols they want in their password
while True:
    print("Welcome to Random Password Generator, you will be presented with some questions to determine \nthe length of your password, please answer with numeric values only (i.e. 5)")
    print("\n")
    password_letters_lower = input("How many lower case letters?: ")
    password_letters_upper = input("How many upper case letters?: ")
    password_digits = input("How many numbers?: ")
    password_symbols = input("How many symbols?: ")

    try:
        password_letters_lower = int(password_letters_lower)
        password_letters_upper = int(password_letters_upper)
        password_digits = int(password_digits)
        password_symbols = int(password_symbols)
        break
    except ValueError:
        print("Invalid entry. Try again.")
        continue

# define our empty string for password
password = ""

# we define our variables of strings so we can pull strings/digits/symbols from here down in our code
letters_lower = string.ascii_lowercase
letters_upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation


# we define our lists
list_letters_lower = []
list_letters_upper = []
list_digits = []
list_symbols = []


# start while loop to generate 10 characters long password
while len(list_letters_lower) < password_letters_lower: 
    # we generate a random letter
    random_letters_lower = random.choice(letters_lower) 
    # we add every random character to the loop/iteration
    list_letters_lower += random_letters_lower

while len(list_letters_upper) < password_letters_upper: 
    # we generate a random letter
    random_letters_upper = random.choice(letters_upper) 
    # we add every random character to the loop/iteration
    list_letters_upper += random_letters_upper
    
while len(list_digits) < password_digits:
    random_digits = random.choice(digits)
    list_digits += random_digits
    
while len(list_symbols) < password_symbols:
    random_symbols = random.choice(symbols)
    list_symbols += random_symbols


# we define password variable and add all the lists together
password_list = list_digits + list_letters_lower + list_symbols + list_letters_upper

# we shuffle the password list with random.shuffle()
random.shuffle(password_list)

# we convert the password list to a string using ''.join() -- '' that determines the separator between strings
password = ''.join(password_list)

# we print the password
print(f"Your password is: {password}")