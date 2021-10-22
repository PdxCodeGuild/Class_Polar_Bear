# Version 1 - Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

# Index  	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
# English	a	b	c	d	e	f	g	h	i	j	k	  l	  m	  n	  o	  p	  q	  r	  s	  t	  u	  v	  w	  x	  y	  z
# ROT+13 	n	o	p	q	r	s	t	u	v	w	x	  y	  z	  a	  b	  c	  d	  e	  f	  g	  h	  i	  j	  k	  l	  m

english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rot_13 =  ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
encript_dict = {}
encript_dict = {english[i]: rot_13[i] for i in range(len(english))}
# print(encript_dict)

# while True:
#   user_word = input('Enter a word: ')
#   ask_which = input('Would you like to encrypt or decript? e/d: ').lower()
#   english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#   rot_13 =  ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
#   if ask_which == 'e':
#     encrypt_dict = {}
#     encrypt_dict = {english[i]: rot_13[i] for i in range(len(english))}
#     encripted_word = ''
#     for letter in user_word:
#       encripted_word += encrypt_dict[letter]
#     print(encripted_word)
#   elif ask_which == 'd':
#     decrypt_dict = {}
#     decrypt_dict = {rot_13[i]: english[i] for i in range(len(english))}
#     decrypted_word = ''
#     for letter in user_word:
#       decrypted_word += decrypt_dict[letter]
#     print(decrypted_word)
#   else:
#     print('Make sure you choose "e" or "d"')
#     continue
#   try_another = input('Another? y/n: ').lower()
#   if try_another == 'y':
#     continue
#   else:
#     break


# Version 2 - Allow the user to input the amount of rotation used in the encryption. (ROTN)

def find_letter(letter, amount, encrypt = False, decrypt = False):
  index = english.index(letter)
  if encrypt:
    if index + amount > len(english) - 1:
      remain = amount - (len(english) - index)
      return english[remain % 26]
    else:
      return english[index + amount]
  if decrypt:
    if index - amount < 0:
      remain = amount - (index - 1)
      return english[(index + 1) - (remain % 26)]
    else:
      return english[index - amount]

while True:
  user_word = input('Enter a word: ')
  rotations = input('Enter amount of rotations: ')
  ask_which = input('Would you like to encrypt or decript? e/d: ').lower()
  english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  if ask_which == 'e':
    encripted_word = ''
    for letter in user_word:
      encripted_word += find_letter(letter, int(rotations), encrypt=True)
    print(encripted_word)
  elif ask_which == 'd':
    decrypted_word = ''
    for letter in user_word:
      decrypted_word += find_letter(letter, int(rotations), decrypt=True)
    print(decrypted_word)
  else:
    print('Make sure you choose "e" or "d"')
    continue
  try_another = input('Another? y/n: ').lower()
  if try_another == 'y':
    continue
  else:
    break


# Version 3 - Implement the Rot Cipher algorithm inside a class.
class RotCipher:

    def __init__(self, rot_amount):
      self.rot_amount = 13
      ...

    def encrypt(self, text):
      encripted_word = ''
      for letter in text:
        encripted_word += find_letter(letter, int(self.rot_amount), encrypt=True)
      return encripted_word
      ...

    def decrypt(self, text):
      decrypted_word = ''
      for letter in text:
        decrypted_word += find_letter(letter, int(self.rot_amount), decrypt=True)
      return decrypted_word
      ...

    def __str__(self):
      ...


rot_cipher = RotCipher(13)

text = 'hello'
encrypted_text = rot_cipher.encrypt(text)
print(encrypted_text) # uryyb
decrypted_text = rot_cipher.decrypt(encrypted_text)
print(decrypted_text) # hello


 ############################ Used recursion ###################################
# def find_letter(letter, amount, encrypt = False, decrypt = False, remain = 0):
#   index = english.index(letter)
#   if encrypt:
#     if index + amount > len(english):
#       remain = amount - (len(english) - index)
#       return find_letter('a', remain, encrypt=True, remain=remain)
#     else:
#       return english[index + amount]

# print(find_letter('y', 28, encrypt=True))