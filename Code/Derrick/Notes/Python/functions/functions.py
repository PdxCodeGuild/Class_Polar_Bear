

# def getUserInput(chars,unit):
    
#     while True:
#         chars = input(f'Enter {unit}')
#         try:
#             chars = int(chars)
#             break
#         except ValueError:
#             print('Invalid')
#     return chars


# lower = 0
# getUserInput(lower,'lower')

# upper = 0
# getUserInput(upper,'upper')

# numbers = 0
# getUserInput(numbers,'numbers')

# symbols = 0
# getUserInput(symbols,'symbols')

# def add(num1,num2=1): # creates default value for an argument
#     return num1 + num2

# # keyword arguments
# # gives default value

# # positional arguments 
# # need a value to be specified to work
# # these need to come before any keyword arguments
# # can provide these in any order

# print(add(10))

def greeting(msg='hello',n=1):
    return msg * n

print(greeting(n=4)) #keyword arguments need to be redefined to only use one argument
print(greeting(msg='Good Evening'))