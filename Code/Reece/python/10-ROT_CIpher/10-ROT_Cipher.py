# Reece Adams - lab 10 in class - mob 10 - Rot Cipher #

# Version 1 --- Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption. --- #
'''
Index 	    0 	1 	2 	3 	4 	5 	6 	7 	8 	9 	10 	11 	12 	13 	14 	15 	16 	17 	18 	19 	20 	21 	22 	23 	24 	25
English 	a 	b 	c 	d 	e 	f 	g 	h 	i 	j 	k 	l 	m 	n 	o 	p 	q 	r 	s 	t 	u 	v 	w 	x 	y 	z
ROT+13 	    n 	o 	p 	q 	r 	s 	t 	u 	v 	w 	x 	y 	z 	a 	b 	c 	d 	e 	f 	g 	h 	i 	j 	k 	l 	m
'''

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# rot_13 = 'nopqrstuvwxyzabcdefghijklm'
# text = input('Enter your text to encrypt: ')

# def encrypt(text):
#     encrypted_text = ''
#     for char in text:
#         index_value = alphabet.find(char)
#         encrypted_text += rot_13[index_value]
#         # print(alphabet.find(char))
#     return encrypted_text

# print(encrypt(text))

# Version 2 --- Allow the user to input the amount of rotation used in the encryption. (ROTN) --- #
# '''
# Index 	    0 	1 	2 	3 	4 	5 	6 	7 	8 	9 	10 	11 	12 	13 	14 	15 	16 	17 	18 	19 	20 	21 	22 	23 	24 	25
# English 	a 	b 	c 	d 	e 	f 	g 	h 	i 	j 	k 	l 	m 	n 	o 	p 	q 	r 	s 	t 	u 	v 	w 	x 	y 	z
# '''

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# text = input('Enter your text to encrypt: ')
# rotn = input('Please enter your shift amount as an integer: ')

# try:
#     rotn = int(rotn)
# except ValueError:
#     rotn = input('Invalid input...Please enter your shift amount as an integer: ')
# rotn = int(rotn)

# def encrypt(text, shift):
#     encrypted_text = ''
#     for char in text:
#         if char.lower() in alphabet:
#             encrypted_index = alphabet.index(char) + shift
#             encrypted_text += alphabet[encrypted_index % 26]
#         else:
#             encrypted_text += 1
#     return encrypted_text

# print(encrypt(text, rotn))

# Version 3 # --- Implement the Rot Cipher algorithm inside a class. --- #
'''
Index 	    0 	1 	2 	3 	4 	5 	6 	7 	8 	9 	10 	11 	12 	13 	14 	15 	16 	17 	18 	19 	20 	21 	22 	23 	24 	25
English 	a 	b 	c 	d 	e 	f 	g 	h 	i 	j 	k 	l 	m 	n 	o 	p 	q 	r 	s 	t 	u 	v 	w 	x 	y 	z
ROT+13 	    n 	o 	p 	q 	r 	s 	t 	u 	v 	w 	x 	y 	z 	a 	b 	c 	d 	e 	f 	g 	h 	i 	j 	k 	l 	m
'''

from typing import Text


class RotCipher:

    def __init__(self, rot_amount):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.rot_amount = rot_amount
        self.text = user_input
        ...
    
    def encrypt(self, text):
        temp_str = ''
        for i in text.lower():
            posi_index = self.alphabet.index(i)
            if posi_index >= 13:
                posi_index -= 26
            new_index = posi_index + self.rot_amount
            temp_str += self.alphabet[new_index]
        return temp_str
        ...
    
    def decrypt(self, text):
        # print(text + ' this is it')
        temp_str = ''
        for i in text:
            posi_index = self.alphabet.index(i)
            if posi_index <= 12:
                posi_index +=26
            new_index = posi_index - self.rot_amount
            temp_str += self.alphabet[new_index]
        return temp_str
    
    def __str__(self):
        ...


user_input = input('Enter your text: ')

rot_cipher = RotCipher(13)

text = user_input
encrypted_text = rot_cipher.encrypt(text)
print(encrypted_text) # uryyb
decrypted_text = rot_cipher.decrypt(encrypted_text)
print(decrypted_text) # hello