# Reece Adams - lab14.py - lab 14 - Automated Readability Index #

import string

# Defining ------------------------------------------------------------------------------#

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

characters = (string.ascii_letters + string.digits)

def sentence_check(text):
    sentence_count = 0
    for char in text:
        if char == '.':
            sentence_count += 1
    return sentence_count

def word_check(text):
    split_text = text.split()
    return len(split_text)

def character_check(text):
    character_count = 0
    for char in text:
        if char in characters:
            character_count += 1
    return character_count

#-----------------------------------------------------------------------------------------#

with open('lab14_book.txt', encoding='utf-8') as book:
    text = book.read().lower()

# Sentence Count ------------------------------------------------------------------------#

sentence_count = sentence_check(text)

# Word Count ---------------------------------------------------------------------------#

word_count = word_check(text)

# Character Count -----------------------------------------------------------------------#

character_count = character_check(text)

# ARI Calculations ----------------------------------------------------------------------#

ARI_level = int(4.71*(character_count/word_count) + 0.5*(word_count/sentence_count) -
                21.43) + (4.71*(character_count % word_count) + 0.5*(word_count % sentence_count) - 21.43 > 0)

if ARI_level > 14:
    ARI_level = 14

for key in ari_scale:
    if key == ARI_level:
        print(f'\nThe ARI level of lab14_book.txt is {ARI_level}.\nThis corresponds to a {ari_scale[ARI_level]["grade_level"]} Grade level of difficulty.\nThis would be suitable for someone {ari_scale[ARI_level]["ages"]}.\n')