
import string

with open('twain.txt', 'r', encoding='utf-8') as file:
    text = file.read()


new_text = text.lower()

new_text = new_text.replace('\n', " ")

for x in string.punctuation:
    new_text = new_text.replace(x, "")


text_list = new_text.split(" ")



def count():
# word_dict is a dictionary where the key is the word and the value is the count
    word_dict = {}

    for word in text_list:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1
    return word_dict

word_dict = count(text)

words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
