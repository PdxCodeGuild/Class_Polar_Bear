import random
import string

special_character = (string.punctuation)
letters = (string.ascii_letters)
numbers = (string.digits)

#Creating the list of all potential password characters
all_characters = special_character + letters + numbers

password = []

#Requesting the length of desired password
requested_length = input('Please enter the number of characters you want your password to be? ')
requested_length = int(requested_length)
#Adjusting for the count starting at 0
password_length = requested_length - 1

#Generating the random password
while len(password) <= password_length:
    password.append(random.choice(all_characters))

print(f'Your password is: {"".join(password)}')




