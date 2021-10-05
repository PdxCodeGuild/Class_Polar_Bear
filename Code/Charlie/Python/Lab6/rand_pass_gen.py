
import random
import string


generate = '' 
generate = list(generate)

user_input_uc = int(input('How many upper case letters would you like? '))
for i in range(user_input_uc):
    generate += random.choice(string.ascii_uppercase)

user_input_lc = int(input('How many lower case letters would you like? '))
for i in range(user_input_lc):
    generate += random.choice(string.ascii_lowercase) 

user_input_num = int(input('How many numbers would you like? '))
for i in range(user_input_num):
    generate += random.choice(string.digits) 

user_input_sc = int(input('How many special characters would you like? '))
for i in range(user_input_sc):
    generate += random.choice(string.punctuation) 

random.shuffle(generate)
generate = ''.join(generate)
print(generate)





# turn into while loop
# append all input to a list
# -= all other inputs from user_input

# password = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
# generate_list = []
# upper_case = password[0:25]
# lower_case = password[0:25]
# num = password[26:35]
# special = password[36:]

# i = 0
# while i < user_input:
#     generate += random.choice(password)
#     i += 1 		# i = i + 1





# for i in range(user_input):
#     generate += random.choice(password)
#     print(generate)
# print(f' Here is your {user_input} character password')