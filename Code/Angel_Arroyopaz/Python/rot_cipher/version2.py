import string

# define english alphabet
english = string.ascii_lowercase
english = list(english)

# define function to encrypt
def encrypt(user_input_list, rotation=13):
    cipher = ''
    for letter in user_input_list:
        if letter in english:
            formula = (english.index(letter) + rotation) % 26
            cipher += english[formula]
            
    return cipher

# prompt user for a string
user_input = input("Enter a string: ").lower().replace(" ", "")

# prompt user for rotation number
rotation = int(input("Enter the amount of rotation for the encryption algorithm: "))

# convert to a list
user_input_list = list(user_input)

# encode string with ROT13. For each character, find the corresponding character
# add it to an output string.
output = encrypt(user_input_list, rotation)

print(f'Input: {user_input} ---> Output: {output}')