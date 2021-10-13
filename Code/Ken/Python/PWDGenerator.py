# Password Generator

import random
import string

pwd_characters = []

user_input = input("How many characters would you like your new Password to be?:  ")
user_input = int(user_input)

while len(pwd_characters) < user_input:

    random_character = random.choice(string.ascii_letters + string.digits + string.punctuation)

    pwd_characters.append(random_character)

    listToStr = "".join(pwd_characters)



print(f"Your new password is:  {listToStr}")