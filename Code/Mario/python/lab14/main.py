
# print(text)

# word_dict = {}

# for word in text:
#     word_dict[word] = len(word)
# print(word_dict)

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

formula = round(((char_count / word_count * 4.71) +
                 0.5 * (word_count/sentences) - 21.43))
ari_score = str(formula)
print(type(ari_score))

# TODO-------------------------------------------------------------------------

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

for x in ar
