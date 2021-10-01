import random
import string

all_letters = string.ascii_letters
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
numbers = string.digits
special_characters = string.punctuation

# All choices:
# all_possible_chars = all_letters + str(numbers) + special_characters
# while True:
#   n = input('\nHow long do you wish your password to be? Enter a number: ')
#   i = 0
#   password = ''
#   try:
#     n = int(n)
#     break
#   except ValueError:
#     print('Please enter a number')
# while i < n:
#   password += random.choice(all_possible_chars)
#   i+=1
# print(f'\nYour new password is: {password}')

# Individual choices
print('Welcome to password generator!')
while True:
  lower_amount = input('\nHow many lower case letters? ')
  upper_amount = input('How many upper case letters? ')
  numbers_amount = input('How many numbers? ')
  special_characters_amount = input('How many special characters? ')
  password = ''
  l = ''
  u = ''
  n = ''
  sc = ''
  try:
    lower_amount = int(lower_amount)
    upper_amount = int(upper_amount)
    numbers_amount = int(numbers_amount)
    special_characters_amount = int(special_characters_amount)
    break
  except ValueError:
    print('\nOnly enter numbers! Try Again')

i = 0
while i < lower_amount:
  l += random.choice(lower_case)
  i+=1

i = 0
while i < upper_amount:
  u += random.choice(upper_case)
  i+=1

i = 0
while i < numbers_amount:
  n += random.choice(numbers)
  i+=1

i = 0
while i < special_characters_amount:
  sc += random.choice(special_characters)
  i+=1

# First to shuffle password
# total_passowrd_length = len(l) + len(u) + len(n) + len(sc)
# i = 0
# while i < total_passowrd_length:
#   password += random.choice(l + u + n + sc)
#   i+=1

# Second to shuffle password
password = l + u + n + sc
password = list(password)
random.shuffle(password)
password = ''.join(password)

print(f'\nThis is your new password: {password}')

