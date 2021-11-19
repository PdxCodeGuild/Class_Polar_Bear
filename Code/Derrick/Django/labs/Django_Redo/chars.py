import random 
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
letters = string.ascii_letters
options = ['uppercase letters','lowercase letters','symbols','numbers']


## functions ##

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

def allChars(a,b,c,d):   
    final_password = numOfUpper(a) + numOfLower(b) + numOfSymbols(c) + numOfNumbers(d)
    final_password = list(final_password)
    random.shuffle(final_password)
    final_password = ''.join(final_password)
    return f'Your password of {a} {options[0]}, {b} {options[1]}, {c} {options[2]} and {d} {options[3]} is: {final_password}'
    
def numOfUpper(n):
    i = 0
    upper_letters = ''
    while i < int(n): 
        upper_letters += str(random.choice(upper))
        i += 1
    return upper_letters

def numOfLower(n):
    i = 0
    lower_letters = ''
    while i < int(n): 
        lower_letters += str(random.choice(lower))
        i += 1
    return lower_letters
def numOfSymbols(n):
    i = 0
    num_of_symbols = ''
    while i < int(n): 
        num_of_symbols += str(random.choice(symbols))
        i += 1
    return num_of_symbols
def numOfNumbers(n):
    i = 0
    num_of_numbers = ''
    while i < int(n): 
        num_of_numbers += str(random.choice(numbers))
        i += 1
    return num_of_numbers