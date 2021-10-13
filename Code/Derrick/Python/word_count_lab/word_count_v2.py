import string

symbols = string.punctuation
word_dict = {}
new_word_list = []


with open('saboteur_of_space.txt', 'r', encoding='utf-8') as file:
    plain_text = file.read().lower().strip()
    plain_text = plain_text.replace('\n',' ')

    for char in plain_text:
        if char in symbols:
            if char == "'":
                plain_text = plain_text.replace(char,'')
            else:
                plain_text = plain_text.replace(char,' ')
    
    word_list = plain_text.split(' ')

    while '' in word_list:
        word_list.remove('')


for i in range(len(word_list)):
    try:
        if i % 2 == 0:
            new_word_list.append(word_list[i] + ' ' + word_list[i+1])
    except IndexError:
        break

for pair in new_word_list:
    if word_dict.get(pair) == None:
        word_dict[pair] = 1
    else:
        word_dict[pair] += 1


words = list(word_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])