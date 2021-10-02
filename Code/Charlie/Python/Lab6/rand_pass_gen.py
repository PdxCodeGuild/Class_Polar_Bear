

import random


user_input = int(input('Choose a number length for your password '))
# user_input_uc = int(input('How many upper case letters would you like '))
# user_input_lc = int(input('How many lower case letters would you like? '))
# user_input_num = int(input('How many numbers would you like '))
# user_input_sc = int(input('How many special characters would you like '))

password = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'

generate = ' ' 
upper_case = password[0:25]
lower_case = password[0:25]
num = password[26:35]
special = password[36:]

# turn into while loop
# append all input to a list
# -= all other inputs from user_input

i = 0
while i < user_input:
    generate += random.choice(password)
    i += 1 		# i = i + 1





# for i in range(user_input):
#     generate += random.choice(password)
#     print(generate)

# for i in range(user_input_uc):
#     generate += random.choice(upper_case.upper())

# for i in range(user_input_lc):
#     generate += random.choice(lower_case.lower()) 

# for i in range(user_input_num):
#     generate += random.choice(num) 

# for i in range(user_input_sc):
#     generate += random.choice(special) 



print(f' Here is your {user_input} character password')
print(generate) 