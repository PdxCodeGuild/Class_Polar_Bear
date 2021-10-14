

with open("../lab15/book.txt", encoding="utf-8") as file:
    text = file.read().strip().split(' ')

char_count = 0
word_count = 0
sentences = 0

for word in text:
    # print(word)
    char_count += len(word)
    word_count += 1
    if "." in word:
        sentences += 1

score = round(((char_count / word_count * 4.71) +
               0.5 * (word_count/sentences) - 21.43))
if score > 14:
    score = 14
ari_score = str(score)

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

grade_level = ari_scale[score]['grade_level']
age = ari_scale[score]['ages']
print(f'''The ARI for  The Arabian Nights.txt is {ari_score}
This corresponds to a {grade_level} level of difficulty
that is suitable for an average person {age} years old.''')

# for scale in ari_scale:
#     val = ari_scale[scale]['ages'].split('-')[0]

#     if val == ari_score or test > 18:
#         if test > 18:
#             print(f'''The ARI for  The Arabian Nights.txt is {ari_score}
#     This corresponds to a college level of difficulty
#     that is suitable for an average person 18-22 years old.''')
#             break
#         else:
#             grade_level = ari_scale[scale]['grade_level']
#             age = ari_scale[scale]['ages']
#             print(f'''The ARI for  The Arabian Nights.txt is {ari_score}
#     This corresponds to a {grade_level} level of difficulty
#     that is suitable for an average person {age} years old.''')
