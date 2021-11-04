import string

with open('metamorphosis.txt', 'r', encoding='utf-8') as file:
    book = file.read()

for p in string.punctuation:
    book = book.replace(p, '')

book = book.lower()
book_list = book.split(' ')

book_dict = {}
for word in book_list:
    book_dict[word] = book_dict.get(word, 0) + 1

words = list(book_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])

