import string

alphabet = string.ascii_lowercase

class RotCipher:

    def __init__(self, rot_amount=13):
        self.rot_amount = rot_amount

    def encrypt(self, text):
        s = ''
        for char in text:
            s += alphabet[(alphabet.index(char) + self.rot_amount)%26]
        return s
    
    def decrypt(self, text):
        s = ''
        for char in text:
            s += alphabet[alphabet.index(char) - self.rot_amount]
        return s
    
    def __str__(self):
        return f'Rot Cipher amount is {self.rot_amount}'

rot_cipher = RotCipher(13)

text = 'hello'
encrypted_text = rot_cipher.encrypt(text)
print(encrypted_text) # uryyb
decrypted_text = rot_cipher.decrypt(encrypted_text)
print(decrypted_text) # hello

