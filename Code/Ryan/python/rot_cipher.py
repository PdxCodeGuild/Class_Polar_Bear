

# letters =['a', 'b',	'c',	'd',	'e',	'f',	'g',	'h',	'i',	'j',	'k',	'l',	'm',	'n',	'o',	'p',	'q',	'r',	's',	't',	'u',	'v',	'w',	'x',	'y',	'z']

# letters = list(ascii_lowercase)

# user_string = list(input("Please enter a string to be encoded: ").lower())

# rotn = int(input('Enter the amount of rotations used in the encoding (1-26): '))
# rotn -= 1
# user_input = ''.join(user_string)

# for i in range(len(user_string)):
#     for place in range(len(letters)):
#         if user_string[i] == letters[place]:
#             rot13 = place + rotn #13 for version 1
#             # print(rot13)
#             if rot13 > 25:
#                 rot13 -= 26
#                 # print(rot13)
#             user_string[i] = letters[rot13]
#             # print(user_string[i])
#             break

# cipher = ''.join(user_string)

# print(f'{user_input} ----> {cipher}')
from string import ascii_lowercase


# print(list(ascii_lowercase))

class RotCipher:

    def __init__(self, rot_amount=13):
        if rot_amount < 25:
            self.rot_amount = rot_amount
        ...
    
    def encrypt(self, text):
        text = list(text)
        key = list(ascii_lowercase)
        for i in range(len(text)):
            for letter in range(len(key)):
                if text[i] == key[letter]:
                    self.encrypt = letter + self.rot_amount
                    if self.encrypt > 25:
                        self.encrypt -= 26
                    text[i] = key[self.encrypt]
                    break
        return ''.join(text)


        ...
    
    def decrypt(self, text):
        text = list(text)
        key = list(ascii_lowercase)
        for i in range(len(text)):
            for letter in range(len(key)):
                if text[i] == key[letter]:
                    self.decrypt = letter - self.rot_amount
                    if self.decrypt > 0:
                        self.encrypt += 26
                    text[i] = key[self.decrypt]
                    break
        return ''.join(text)        
        
        
        ...
    
    def __str__(self):
        ...


rot_cipher = RotCipher(13)

text = 'hello'
encrypted_text = rot_cipher.encrypt(text)
print(encrypted_text) # uryyb
decrypted_text = rot_cipher.decrypt(encrypted_text)
print(decrypted_text) # hello
