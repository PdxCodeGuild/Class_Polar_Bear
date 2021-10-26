'''Rot Cipher
Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.
example input/output:
hello -> uryyb
world -> jbeyq
llama -> yynzn

Version 2
Allow the user to input the amount of rotation used in the encryption. (ROTN)
Version 3 ()
Implement the Rot Cipher algorithm inside a class.
class RotCipher:

    def __init__(self, rot_amount):
        ...
    
    def encrypt(self, text):
        ...
    
    def decrypt(self, text):
        ...
    
    def __str__(self):
        ...


rot_cipher = RotCipher(13)

text = 'hello'
encrypted_text = rot_cipher.encrypt(text)
print(encrypted_text) # uryyb
decrypted_text = rot_cipher.decrypt(encrypted_text)
print(decrypted_text) # hello'''