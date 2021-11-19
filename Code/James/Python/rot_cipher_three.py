'''
___________________________________________________________________________
Project: Full Stack Evening Boot Camp - Python Lab 10 (Rot Cypher)
    Version: 3.0
Author: James Thornton
  Email: James.ed.thornton@gmail.com
Date: 21 OCT 2021
___________________________________________________________________________
'''

# V3: Implement the Rot Cipher algorithm inside a class.

class RotCipher:

    def __init__(self, rot_amount):
        self.user_list = []
        self.user_list_decrypt = []
    
    def encrypt(self, text):

        # Create user list
        user_string = text
        for character in user_string:
            self.user_list.append(character)
        # print(user_list)

        # Create ABC list
        abc = 'abcdefghijklmnopqrstuvwxyz'
        abc_list = []
        for character in abc:
            abc_list.append(character)
        # print (abc_list)

        # Apply cipher to ABC list
        import collections
        rotation = 13
        abc_object = collections.deque(abc_list)
        abc_object.rotate(int(rotation))
        rotated_list = list(abc_object)
        # print(output_list)

        # Build cipher dictionary
        cipher_dict = dict(zip(abc_list,rotated_list))
        # print(cipher_dict)

        # Translate user list
        translated_list = []
        for letter in self.user_list:
            # find letter in cipher_dict
            for character in cipher_dict:
                if character == letter:
                    # replace corresponding letter in cipher_dict into user_list
                    translated_letter = cipher_dict[character]
                    translated_list.append(translated_letter)
        # print(translated_list)  

        # Join user list into string
        encrypted_output = ''.join(translated_list)

        # Return encrypted_text
        return encrypted_output
# --------------------------------------------------------------- End of def encrypt    

    def decrypt(self, text):
        # Create user list
        user_string = text
        for character in user_string:
            self.user_list_decrypt.append(character)
        # print(user_list)

        # Create ABC list
        abc = 'abcdefghijklmnopqrstuvwxyz'
        abc_list = []
        for character in abc:
            abc_list.append(character)
        # print (abc_list)

        # Apply cipher to ABC list
        import collections
        rotation = -13
        abc_object = collections.deque(abc_list)
        abc_object.rotate(int(rotation))
        rotated_list = list(abc_object)
        # print(output_list)

        # Build cipher dictionary
        cipher_dict = dict(zip(abc_list,rotated_list))
        # print(cipher_dict)

        # Translate user list
        translated_list = []
        for letter in self.user_list_decrypt:
            # find letter in cipher_dict
            for character in cipher_dict:
                if character == letter:
                    # replace corresponding letter in cipher_dict into user_list
                    translated_letter = cipher_dict[character]
                    translated_list.append(translated_letter)
        # print(translated_list)  

        # Join user list into string
        decrypted_output = ''.join(translated_list)

        # Return encrypted_text
        return decrypted_output

        ...
# --------------------------------------------------------------- End of def decrypt

    
    def __str__(self):
        '''user_string = text
        for character in user_string:
            self.user_list.append(character)'''

rot_cipher = RotCipher(13)

text = 'hello'
encrypted_text = rot_cipher.encrypt(text)
print(encrypted_text) # uryyb
decrypted_text = rot_cipher.decrypt(encrypted_text)
print(decrypted_text) # hello
