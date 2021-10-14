import re
import string

# Read lab13.txt

with open('lab13_book.txt', encoding='utf-8') as book:
    # book_text = book.read().replace(',','').replace('.','').lower()
    book_text = book.read().lower()

# remove edge cases that may impact word count

for char in string.punctuation + '——'+ '——' + '”' + '“' + '’':
    book_text = book_text.replace(char,'').lower()

# split book_text

with open('lab13_split_book.txt')as split_book:
    split_book = book_text.split(' ')



# search for word

word = input('Look up a word: ')

loop = True

book_dict = {}

for i in range(len(split_book)-1):
    if split_book[i] in book_dict:
        book_dict[split_book[i]].append(split_book[i])

print(book_dict)
# while loop:
#     found_word = False
#     for i in range(len(split_book)):
#         if word.lower() == i in split_book:
#             print(word + i)
#             found_word = True
#     if word.lower() != found_word:
#         word = input('No match found...Look up a new word: ')
#         if word.lower() == i in split_book:
#             print(word + i)
#             found_word = True
#             loop = False





# found_entry = False
# for entry in phonebook:
#     if name.lower() in entry.lower():
#         print(entry)
#         found_entry = True

# if i in index == 'input_word' print(word and index place in an f string)


# with open('lab13_split_book.txt', 'w')as split_book:
#     split_book.write(book_text.split(' '))


# with open('data/colors.txt', 'w') as file:
    # colors = file.read().split(', ')

# with open('data/colors.txt', 'w') as file:
#     file.write('\n'.join(colors))

print()
