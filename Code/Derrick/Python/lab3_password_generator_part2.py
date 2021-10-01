import random
import string

numbers = string.digits
symbols = string.punctuation
upper = string.ascii_uppercase
lower = string.ascii_lowercase

upper_count = input('How many uppercase letters do you want?')
lower_count = input('How many lowercase letters do you want?')
symbol_count = input('How many symbols do you want?')
num_count = input('How many numbers do you want?')

def allChars(a,b,c,d):   
    final_password = numOfUpper(a) + numOfLower(b) + numOfSymbols(c) + numOfNumbers(d)
    final_password = list(final_password)
    random.shuffle(final_password)
    final_password = ''.join(final_password)
    print(final_password)
    
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

allChars(upper_count,lower_count,symbol_count,num_count)