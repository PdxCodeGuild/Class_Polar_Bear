# Reece Adams- lab13.py

# https://www.gutenberg.org/cache/epub/66563/pg66563.txt

import string

# Read lab13.txt

with open('book.txt', encoding='utf-8') as book:
    book_text = book.read().lower()

# remove edge cases that may impact word count

for char in string.punctuation + '“’”—':
    book_text = book_text.replace(char,'').lower()

print(book_text)

# split book_text

with open('lab13_split_book.txt')as split_book:
    split_book = book_text.split(' ')

print(split_book)