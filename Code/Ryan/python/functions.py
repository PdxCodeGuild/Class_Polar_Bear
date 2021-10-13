# def get_unit_lenth(message):
#     while True:
#         unit = input(message)
#         try:
#             unit = int(unit)
#             break
#         except ValueError:
#             print('invalid input')
#     return unit #, message #tuples are immutable lists

# lower_char = get_unit_lenth('enter the lower charactrs: ')

# upper_char = get_unit_lenth('enter the upper characters: ')

# digits = get_unit_lenth('enter the digits: ')

# special_char = get_unit_lenth('enter the special characters: ')

# print(lower_char, upper_char, digits, special_char)


# def add(num1, num2): 
#     # positional arguments must have an input (the def has no value)
#     # keyword argument has a value and user input can be left blank; keyword arguments can be in any order
#     # print(add(num2=4, num1=8))
#     result = num1 + num2
#     return result

# print(add(2, 3)) #this is positional argument because it matches up with the function

# def greeting(message, number=1):
#     #repeat given message n nmuber of times
#     print(message * number) #number times a string will print that string that many times
#     # all functions inherently set to return None 
# greeting('hello world')

