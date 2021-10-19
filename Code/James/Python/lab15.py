'''
___________________________________________________________________________
Project: Full Stack Evening Boot Camp - Python Lab 15 (Count Words)
    Version: 1.0
Author: James Thornton
  Email: James.ed.thornton@gmail.com
Date: 11 OCT 2021
___________________________________________________________________________
'''

with open('book.txt', 'r', encoding = 'utf-8') as file:
    text = file.read()

# strip punctuation and make lowercase
'''
import re
unpunctuated = re.sub(r'[^\w\s]','',text)
unpunctuated2 = unpunctuated.strip("''")
book = unpunctuated2.lower()
'''

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
book = ""
for x in text:
    if x not in punctuation:
        book=book+x

book_lower = book.lower()

# split words into list

word_list = book_lower.split(' ')

# print(word_list)

# put words into dictionary

word_dict = {} # word_dict is a dictionary where the key is the word and the value is the count

for word in word_list:
    word_dict[word] = word_dict.setdefault(word, 0) + 1

words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(10):  # print the top 10 words, or all of them, whichever is smaller
     print(words[i])
