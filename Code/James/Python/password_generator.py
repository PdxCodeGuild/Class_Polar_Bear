'''
___________________________________________________________________________
Project: Full Stack Evening Boot Camp - Python Lab (06 Password Generator)
    Version: 1.0
Author: James Thornton
  Email: James.ed.thornton@gmail.com
Date: 27 SEP 2021
___________________________________________________________________________
'''

import string
import random

characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.hexdigits + string.punctuation

password_list = []

user = int(input("Enter an integer for how many characters you prefer in your password: "))

i = 1

while i < user:
    password_list.append(random.choice(characters))
    i += 1

password = "".join(password_list)

print(f'Your password is \"{password}"')