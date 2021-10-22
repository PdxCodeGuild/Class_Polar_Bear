import string

# define english alphabet
english = string.ascii_lowercase
english = list(english)

class RotCipher:

    def __init__(self, rotation):
        self.rot_amount = rotation
    
    def encrypt(self, text):
        cipher = ''
        text = list(text)
        for letter in text:
            if letter in english:
                formula = (english.index(letter) + self.rot_amount) % 26
                cipher += english[formula]
            
        return cipher
    
    def decrypt(self, text):
        cipher = ''
        text = list(text)
        for letter in text:
            if letter in english:
                formula = (english.index(letter) - self.rot_amount) % 26
                cipher += english[formula]            

        return cipher


text = input('Enter a word here: ').lower().replace(" ", "")
rotation = int(input('Enter the desired rotation number for the encryption: '))
rot_cipher = RotCipher(rotation)
encrypted_text = rot_cipher.encrypt(text)
decrypted_text = rot_cipher.decrypt(encrypted_text)

print(f'Input: {text} ---> Encryption: {encrypted_text} ---> Decryption: {decrypted_text}')