# ########################## VERSION ONE       #####################

# # import string
# # english = 'abcdefghijklmnopqrstuvwxyz'
# # rot13 = 'nopqrstuvwxyzabcdefghijklm'


# # new_code = ''


# # for index in range(len(password)):
# #     english_index = english.index(password[index])
# #     new_code += rot13[english_index]
# # print(new_code)

# ##########################    VERSION TWO   #####################
# import string
# english = 'abcdefghijklmnopqrstuvwxyz'
# password = 'hello'  # should equal nop
# rotn = int(input('Amount of rotations?: '))
# new_code = ''

# current_index = 0
# for index in range(len(password)):
#     current_index = english.index(password[index]) + rotn
#     if current_index > 25:
#         current_index = current_index - 26
#         new_code += english[current_index]
#     else:
#         new_code += english[current_index]
# print(new_code)

##########################    VERSION three   #####################
class RotCipher:

    def __init__(self, rot_amount):
        self.rotn = rot_amount
        self.english = 'abcdefghijklmnopqrstuvwxyz'

    def encrypt(self, text):
        current_index = 0
        new_code = ''
        for index in range(len(text)):
            current_index = self.english.index(text[index]) + self.rotn
            if current_index > 25:
                current_index = current_index - 26
                new_code += self.english[current_index]
            else:
                new_code += self.english[current_index]
        return new_code
# TODO go back and read this again to make more sense.

    def decrypt(self, text):
        current_index = 0
        new_code = ''
        for index in range(len(text)):
            current_index = self.english.index(text[index]) - self.rotn
            if current_index < 0:
                current_index = current_index + 26
                new_code += self.english[current_index]
            else:
                new_code += self.english[current_index]
        return new_code

    def __str__(self):
        ...


rot_cipher = RotCipher(13)

text = 'hello'
encrypted_text = rot_cipher.encrypt(text)
print(encrypted_text)  # uryyb
decrypted_text = rot_cipher.decrypt(encrypted_text)
print(decrypted_text)  # hello
