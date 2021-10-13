'''
___________________________________________________________________________________
Project: Full Stack Evening Boot Camp - Python Lab 14 (Automated Readability Index)
    Version: 1.0
Author: James Thornton
  Email: James.ed.thornton@gmail.com
Date: 12 OCT 2021
___________________________________________________________________________________
'''

with open('book.txt', 'r', encoding = 'utf-8') as file:
    text = file.read()

# Count sentences

sentences = 0
for character in text:
    if character == ".":
        sentences += 1
for character in text:
    if character == "..":
        sentences -= 1
# print(sentences)

# Count words

words = 0
for character in text:
    if character == " ":
        words += 1
# print(words)

# Count characters

characters = 0
for character in text:
    if character in "abcdefghijklmnopqrstuvwxyz":
        characters += 1
# print(characters)

# Calculate ARI

ARI = 4.71 * characters / words + 0.5 * words / sentences - 21.43
# print(ARI)

# Find age range and grade level

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

ARI_round = round(ARI)
# print(ari_scale[ARI_round])

# Produce output

print("--------------------------------------------------------")
print(f"The ARI for Hawaiian Legends of Volcanoes (mythology) is {ARI_round}")
print(f"This corresponds to a {ari_scale[ARI_round]['grade_level']} level of difficulty")
print(f"That is suitable for an average person {ari_scale[ARI_round]['ages']} years old")
print("--------------------------------------------------------")
