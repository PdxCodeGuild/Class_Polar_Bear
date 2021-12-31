# Reece Adams- lab13.py

# https://www.gutenberg.org/cache/epub/66563/pg66563.txt

import string

# Read lab13.txt

with open('lab13_book.txt', encoding='utf-8') as book:
    book_text = book.read().lower()

# remove edge cases that may impact word count

for char in string.punctuation:
    book_text = book_text.replace(char,'').lower()

for char in '\n':
    book_text = book_text.replace(char, ' ')

# split book_text

split_book_text = book_text.split(' ')

# make a list

word_list = {}
for i in range(len(split_book_text)):
    current_word = split_book_text[i]
    if current_word in word_list:
        word_list[current_word] += 1
    else:
        word_list[current_word] = 1

# print word list

words = list(word_list.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])