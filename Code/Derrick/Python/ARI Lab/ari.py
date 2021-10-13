# characters, words, sentences
import string
import re

book = 'saboteur_of_space.txt'

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

def ARI_formula(characters,words,sentences):
    x = (4.71 * (characters / words)) + (0.5* (words / sentences)) - 21.43
    level = round(x)
    key = ari_scale[level]

    ages = key['ages']
    grade_level = key['grade_level']

    return f'''
    {'-'*50}
    The ARI for {book} is {level}
    This corresponds to a {grade_level} level of difficulty
    that is suitable for an average person {ages} years old.
    {'-'*50}
    '''

with open(book, 'r', encoding='utf-8') as file:
    plain_text = file.read()
    words = plain_text.split()
    words_length = len(words)

    count = 0

    for i in range(len(words)):
        count += len(words[i])

    characters_length = count


with open(book, 'r', encoding='utf-8') as file:
    file = file.read().replace('\n',' ')

    sentence_length = len(re.split('(?<=[.!?]) +',file)) # strips by sentence-ending punctuation
    

print(ARI_formula(characters_length,words_length,sentence_length))
