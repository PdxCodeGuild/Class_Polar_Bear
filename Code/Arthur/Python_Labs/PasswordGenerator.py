"""
Let's generate a password of length n using a while loop and random.choice, 
this will be a string of random characters, e.g. a62xB95. Allow the user to
enter the value of n, remember to convert its type to an int, as input returns a string.
Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

Ask the user for how many lowercase letters,
uppercase letters, numbers, and special characters they'd
like in their password. You do not want the pieces in order
(e.g. 3 lowercase letters followed by 3 uppercase letters...).
You can use list(password_string) or password_string.split('') to
convert the string to a list, random.shuffle(password_list) to shuffle it,
and then ''.join(password_list) to turn it back into a string.
"""

# import random
# import string

# #ask user to enter the password length 
# #characters = string.ascii_letters + string.digits+string.punctuation
# password_choice = string.printable
# while True:
#     password_character=""
#     password_length =int(input("Enter the length of the password :"))
#     for x in range(0,password_length):
#         password_character=password_character + random.choice(password_choice)
#     print(f"password Generated : {password_character}")


# import random
# import string

# #modified


# while True:
#     password =""
#     #we ask the user to enter the length of the password 
#     password_length = int(input("Enter the length of the password :"))
#     #looping through the length
#     for x in range(password_length) :
#         characters = string.digits + string.punctuation + string.ascii_letters
#         password =password +  random.choice(characters)
#     print(f"password Generated : {password}")
    

'''Ask the user for how many lowercase letters,
uppercase letters, numbers, and special characters they'd
like in their password. You do not want the pieces in order
(e.g. 3 lowercase letters followed by 3 uppercase letters...).
You can use list(password_string) or password_string.split('') to
convert the string to a list, random.shuffle(password_list) to shuffle it,
and then ''.join(password_list) to turn it back into a string.
'''
import random
import string

#modified

def verifyifinteger(message) :
    while True:
        length = input(message)
        try:
            length = int(length)
        except ValueError :
            print("Invalid selection, try again:")
        return length

password =""
#we ask the user to enter the length of the password 
lowercase = verifyifinteger("Enter the number of lowercase letters :")
for x in range(lowercase) :
        password = password + random.choice(string.ascii_lowercase)

uppercase = verifyifinteger("Enter the number of uppercase letters :")
for x in range(uppercase):
        password = password + random.choice(string.ascii_uppercase)
    
numbers = verifyifinteger("Enter the how many numbers : ")
for x in range(numbers):
        password = password + random.choice(string.digits)

special_characters = verifyifinteger("Enter the number of special characters: ")    
for x in range(special_characters) :
        password = password + random.choice(string.punctuation)

    #use display the password as a list
passwordlist = list(password)
random.shuffle(passwordlist)


password = "".join(passwordlist)
     
    
print(password)