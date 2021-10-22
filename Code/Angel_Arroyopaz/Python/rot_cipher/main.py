import string

# define english alphabet
english = string.ascii_lowercase
english = list(english)

# define ROT13
rot = 'nopqrstuvwxyzabcdefghijklm'
rot = list(rot)

def encrypt(user_input):
    cipher = ''
    for letter in user_input:
        if letter in english:
            cipher += rot[english.index(letter)]

    return cipher

# prompt user for a string
input = input("Enter a string: ").lower().replace(" ", "")

# convert to a list
user_input = list(input)

# encode string with ROT13. For each character, find the corresponding character
# add it to an output string.
output = encrypt(user_input)

print(f'{input} ---> {output}')