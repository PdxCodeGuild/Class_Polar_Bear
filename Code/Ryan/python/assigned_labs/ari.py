import string
import math


with open('a_tragic_idyl.txt', 'r', encoding='utf-8') as file:
    text = file.read()

sentences = 0
characters = 0
for char in text:
    if char in '.!?':
        sentences += 1
    elif char in string.ascii_letters:
        characters += 1

#checking the punctuation and removing it from the book
# for char in string.punctuation:
#     if char in text:
#         text = text.replace(char, '')

words = len(text.split()) #by default split removes ' ' 

ari = 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43
ari = math.ceil(ari)
if ari > 14:
    ari = 14

# print(f'Sentences: {sentences} \nWords: {words} \nCharacters: {characters}')

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

message = f'''
--------------------------------------------------------
The ARI for A Tragic Idyl is {ari}
This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[ari]['ages']} years old.
--------------------------------------------------------
'''

print(message)