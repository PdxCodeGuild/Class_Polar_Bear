word_dict = {}

# with open('book.txt',  encoding="utf-8") as file:
#     text = file.read()
# # from geeksforgeeks.org
# punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# for word in text:
#     if word in punc:
#         a = text.replace(word, '')
#         with open('words.txt', 'w', encoding="utf-8") as file:
#             file.write(a)

with open('words.txt', encoding="utf-8") as file:
    text = file.read().split(' ')
for word in text:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
words = list(word_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])
