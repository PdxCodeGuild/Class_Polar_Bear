import random
import string

def verify_int(message):
    while True:
        length = input('message')
        try:
            length = int(length)
            break
        except ValueError:
            print('Invalid number, try again.')
    return length

password = ''
lower_letters = ''
uppercase_letters = ''
digits = ''
special_characters = ''


#----------------> trying something new that doesn't work yet <-------------------#
# special_password = [lower_letters, uppercase_letters, digits, special_characters]
# string_characters = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]


# for character in special_password: 
#     character = verify_int(f'Enter number of {character}: ')
#     for x in range(character):
#         password += random.choice(string_characters)

# print(password)


lower_letters = verify_int('Enter number of lowercase letters: ')
for x in range(lower_letters):
    password += random.choice(string.ascii_lowercase)

uppercase_letters = verify_int('Enter number of uppercase letters: ')
for x in range(uppercase_letters):
    password += random.choice(string.ascii_uppercase)

digits = verify_int('Enter number of digits: ')
for x in range(digits):
    password += random.choice(string.digits)

special_characters = verify_int('Enter number of special characters: ')
for x in range(special_characters):
    password += random.choice(string.punctuation)

password_list = list(password)
random.shuffle(password_list)

password = ''.join(password_list)

print(password_list)

