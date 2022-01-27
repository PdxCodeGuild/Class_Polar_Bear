
import string

with open('book.txt', encoding="utf-8") as file:
    text = file.read()

text = text.lower()


for char in string.punctuation + string.digits + '\n”“':
    if char in text:
        text = text.replace(char, "")

text = text.replace("  ", "")


text = text.split(' ')

word_count = {}
for i in range(len(text)):
    current_word = text[i]
    if current_word in word_count:
        word_count[current_word] += 1
    else:
        word_count[current_word] = 1


words = list(word_count.items()) 
words.sort(key=lambda tup: tup[1], reverse=True) 
for i in range(min(10, len(words))):  
    print(words[i])