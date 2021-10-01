import random
import string

# base vars
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
upper = string.ascii_uppercase
lower = string.ascii_lowercase

# user vars
available_chars = letters + numbers + symbols
n = input('Hello, How long do you want your password to be? ')


def passwordGenerator(length,list):
    pw = ''
    
    try:
        length = int(length)
                    
    except ValueError:
        print('Invalid number')
        exit()
        
    while len(pw) < length:
        random_char = random.choice(list)
        pw += random_char

    print(f'Your password is {pw}')

# function

passwordGenerator(n,available_chars)



        





    
    

    


