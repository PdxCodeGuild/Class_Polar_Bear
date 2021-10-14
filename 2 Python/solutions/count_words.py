import string

# Open text file
with open('book.txt', encoding="utf-8") as file:
    text = file.read()


# Make everything lowercase
text = text.lower()

# strip punctuation
for char in string.punctuation + string.digits + '\n”“':
    if char in text:
        text = text.replace(char, "")

text = text.replace("  ", "")


# split into a list of words.
text = text.split(' ')

# Your dictionary will have words as keys and counts as 
# values. If a word isn't in your dictionary yet, add it 
# with a count of 1. If it is, increment its count.
# {
#     'the': 2,
#     'adventures': 1,
#     'of': 3,
#     'sherlock': 1,
#     'panda': 1
# }

word_count = {}
for i in range(len(text)):
    current_word = text[i]
    if current_word in word_count:
        word_count[current_word] += 1
    else:
        word_count[current_word] = 1

# Print the most frequent top 10 out with their counts. 
# You can do that with the code below.
words = list(word_count.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])