import string
import math

book_file='mobydick.txt'
with open(book_file, encoding='utf-8') as file:
    book = file.read()

# Character
char_count=0

for char in book:
    if char != ' ':
        char_count+=1

#Sentences
punct='\"#$%&\'()*+,-/:;<=>@[\]^_`{|}~'
punct_end='.?!'
for char in book:
    if char in punct:
        book = book.replace(char, '')
    if char in punct_end:
        book = book.replace(char, '.')

sen_count=len(book.split('.'))

#Words
for char in book:
    if char in punct_end:
        book = book.replace(char, '')
word_count=len(book.split())

#calculate ari score
ari_score=math.ceil((4.71*(char_count / word_count)) + (0.5*(word_count / sen_count)) - 21.43)
if ari_score > 14:
    ari_score=14

#ari scale
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
book_ari=(ari_scale[ari_score])

age=book_ari['ages']
grade_level=book_ari['grade_level']

print(f'The ARI for {book_file} is {ari_score}.\nThis corresponds to a {grade_level} level of difficulty.\nThat is suitable for an average person {age} years old.')