'''
___________________________________________________________________________
Project: Full Stack Evening Boot Camp - Python Lab (06 Password Generator - Part 2)
    Version: 1.0
Author: James Thornton
  Email: James.ed.thornton@gmail.com
Date: 27 SEP 2021
___________________________________________________________________________
'''

import string
import random

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
special = string.hexdigits + string.punctuation

lowercase_list = []
user = int(input("Enter an integer for how many lowercase letters you prefer in your password: "))
i = 1
while i < user:
    lowercase_list.append(random.choice(lowercase))
    i += 1
lowercase_characters = "".join(lowercase_list)

uppercase_list = []
user2 = int(input("Enter an integer for how many uppercase letters you prefer in your password: "))
i = 1
while i < user2:
    uppercase_list.append(random.choice(uppercase))
    i += 1
uppercase_characters = "".join(uppercase_list)

numbers_list = []
user3 = int(input("Enter an integer for how many lowercase letters you prefer in your password: "))
i = 1
while i < user3:
    numbers_list.append(random.choice(numbers))
    i += 1
numbers_characters = "".join(numbers_list)

special_list = []
user4 = int(input("Enter an integer for how many lowercase letters you prefer in your password: "))
i = 1
while i < user4:
    special_list.append(random.choice(special))
    i += 1
special_characters = "".join(special_list)

password_string = lowercase_characters + uppercase_characters + numbers_characters + special_characters
password_list = list(password_string)
random.shuffle(password_list)
password = "".join(password_list)

print(f'Your password is {password}')