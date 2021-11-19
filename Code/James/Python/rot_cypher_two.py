'''
___________________________________________________________________________
Project: Full Stack Evening Boot Camp - Python Lab 10 (Rot Cypher)
    Version: 2.0
Author: James Thornton
  Email: James.ed.thornton@gmail.com
Date: 21 OCT 2021
___________________________________________________________________________
'''

'''Allow the user to input the amount of rotation used in the encryption. (ROTN)'''

# Create user list
user_string = input("Enter a string: ")
user_list = []
for character in user_string:
    user_list.append(character)
# print(user_list)

# Create ABC list
abc = 'abcdefghijklmnopqrstuvwxyz'
abc_list = []
for character in abc:
    abc_list.append(character)
# print (abc_list)

# Apply cipher to ABC list
import collections
rotation = input('How much rotation would you like in your encryption: ') 
abc_object = collections.deque(abc_list)
abc_object.rotate(int(rotation))
rotated_list = list(abc_object)
# print(output_list)

# Build cipher dictionary
cipher_dict = dict(zip(abc_list,rotated_list))
# print(cipher_dict)

# Translate user list
translated_list = []
for letter in user_list:
    # find letter in cipher_dict
    for character in cipher_dict:
        if character == letter:
            # replace corresponding letter in cipher_dict into user_list
            translated_letter = cipher_dict[character]
            translated_list.append(translated_letter)
# print(translated_list)  

# Join user list into string
translated_string = ''.join(translated_list)
print(translated_string)