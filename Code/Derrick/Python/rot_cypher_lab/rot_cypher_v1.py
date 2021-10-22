import string 

alpha = list(string.ascii_lowercase)
letters = []
word = input('Enter a word to be encoded: ')
output = []

for i in range(len(alpha)):
    if alpha.index(alpha[i]) < 13:
        rot13_letter = alpha[i + 13]
    else:
       rot13_letter = alpha[i - 13] 
    
    letters.append(rot13_letter)

for letter in word:
    output.append(alpha[letters.index(letter)])

print(''.join(output))




