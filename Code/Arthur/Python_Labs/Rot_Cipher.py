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


#function that is going to pass the text and the shift or ROI
def rot_cipher(RotCipher):
   
    Text ='hello'
    RotCipher
    result =[]
    encrpytText =[]

    #we write down the uppercase and lowercase letters
    # uppercase = ['A','B','C','D','E','F','G'
    # ,'H','I','J','K','L','M','N','O','P','Q',
    # 'R','S','T','U','V','W','X','Y','Z']
    # lowercase =['a','b','c','d','e','f','g','h','i',
    # 'j','k','l','m','n','o','p','q','r','s','t','u',
    # 'v','w','x','y','z']

    uppercase ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase ="abcdefghijklmnopqrstuvwxyz"
    


    #for loop to iterate through them
    for letter in Text:
        if letter in uppercase:
            index = uppercase.index(letter)
            encrypting =(index + RotCipher)%26
            encrpytText.append(encrypting)
            shifted_letter = uppercase[encrypting]
            result.append(shifted_letter)
        elif letter in lowercase:
            index = lowercase.index(letter)
            encrypting =(index + RotCipher)%26
            encrpytText.append(encrypting)
            shifted_letter = lowercase[encrypting]
            result.append(shifted_letter)
    return result


# text = 'hello'
# encrypted_text = rot_cipher(text)
# print(encrypted_text) # uryyb

#prompt user to enter the amount of rotation
user_Rotation =int(input("Enter the amount of Rotation: "))
encrypted_text = rot_cipher(user_Rotation)
#print text
print(encrypted_text) # uryyb











