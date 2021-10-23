import string 

alpha = list(string.ascii_lowercase)
rot_alpha = []
rot_num = int(input('Enter number for ROTN: '))
word = input('Enter a word to be encoded: ')
output = []

for i in range(len(alpha)):
    if alpha.index(alpha[i]) < rot_num and i + rot_num <= len(alpha) - 1:
        new_letter = alpha[i + rot_num]
    elif i + rot_num > len(alpha) - 1:
        remainder = len(alpha) - alpha.index(alpha[i]) # q = 16, 25 - 16 = 9, 15-9 = correct letters index
        new_index = rot_num - remainder
        new_letter = alpha[new_index]
        
    rot_alpha.append(new_letter)

for letter in word:
    output.append(rot_alpha[alpha.index(letter)])

print(''.join(output))
