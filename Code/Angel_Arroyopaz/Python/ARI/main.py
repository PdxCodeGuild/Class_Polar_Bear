import string
import math

def letter_separator(text):
    return [char for char in text]

def counter(list):
    total = 0
    for i in range(len(list)):
        total += 1
    return total


def ari(letters, words, sentences):
    return int(math.ceil(((letters / words) * 4.71) + ((words / sentences) + 0.5) - 21.43))

punctuation = string.punctuation + string.digits + "——————————" + "◆⁴" + '\n'

# open file
with open('book.txt') as file:
    text = file.read().lower()

    # split text into sentences and turn into a list
    book_sentence_list = text.split(".")
    sentence_total = counter(book_sentence_list)

    # loop through string to find and remove items in punctuation variable
    for i in text:
        if i in punctuation:
            text = text.replace(i, "")

    # split text into words and turn into a list
    book_word_list = text.split()
    word_total = counter(book_word_list)

    # split text into letters and turn into a list
    book_letter_list = letter_separator(text)
    letter_total = counter(book_letter_list)

    result = ari(letter_total, word_total, sentence_total)
   
    if result > 14:
        result = 14

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

    print(f"The ARI for book is {result}. \nThis corresponds to {ari_scale[result]}")