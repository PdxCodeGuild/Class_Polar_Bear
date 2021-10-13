'''
Password Lab
'''

import random
import string

#assign letters, digits and punctuation
upper_letters=string.ascii_uppercase
lower_letters=string.ascii_lowercase
digits=string.digits

#combine all characters
#all_characters=upper_letters+lower_letters+digits

#split string into list
#char_index=all_characters.split()

welcome='\nWelcome to the password generator!\n'
print(welcome)


'''
Part 1
'''

'''user_pw=[]

while True:
    user_pw_len=input ('How many characters would you like your password to be?: ')

    try:
        pw_len=int(user_pw_len)
    except ValueError:
        print(f'{user_pw_len} is not a number. Please try again.')
        continue

    while len(user_pw)<pw_len:
        user_pw.append(random.choice(all_characters))
    
    user_pw=''.join(user_pw)


    print(f'Your password is: {user_pw}')
    user_pw=[]'''


'''
Part 2
'''

user_pw=[]
upper_char=[]
lower_char=[]
digit_char=[]

while True:
    upper_let_len=input('How many upper case letters would you like your password to have?: ')
    lower_let_len=input('How many lower case letters would you like your password to have?: ')
    digit_len=input('How many numbers would you like your password to have?: ')

    try:
        upper_let_len=int(upper_let_len)
        lower_let_len=int(lower_let_len)
        digit_len=int(digit_len)
    except ValueError:
        print('One of your choices is not a number. Please try again.')
        continue

    while len(upper_char)<upper_let_len:
        upper_char.append(random.choice(upper_letters))
    while len(lower_char)<lower_let_len:
        lower_char.append(random.choice(lower_letters))
    while len(digit_char)<digit_len:
        digit_char.append(random.choice(digits))
    
    user_pw=upper_char+lower_char+digit_char
    random.shuffle(user_pw)
    user_pw=''.join(user_pw)


    print(f'Your password is: {user_pw}')
    break