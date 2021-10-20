import requests
import string
book_dict = {}
# This will pull down a file or book
response = requests.get('https://www.gutenberg.org/ebooks/66517.txt.utf-8')
response.encoding = 'utf-8'
#print(response.text) 
# Take the following steps to build up our dictionary. The result should look something like {'a': 3, 'the': 4}
with open (response.text, 'w', encoding='utf-8') as file:
    file.write(response.text)
# This will print out a file on cmd prmpt
with open(response.text, 'r', encoding='utf-8') as file:
    #this is where you split the book into individual words
    words = file.read().split(' ')

with open(response.text, 'w') as file:
    # Make everything lowercase, strip punctuation, #see above split into a list of words.
    for i in range(len(words)):
        # loop over each letter in word
        for char in words[i]:
            if char in string.punctuation:
                words[i] = words[i].replace(char, "")
            words[i] = words[i].lower()
# Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
        if words[i] in book_dict:
            book_dict[words[i]] += 1
        else:
            book_dict[words[i]] = 1

# Print the most frequent top 10 out with their counts. You can do that with the code below.
# word_dict is a dictionary where the key is the word and the value is the count

word_count = list(book_dict.items()) # .items() returns a list of tuples
word_count.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(word_count))):  # print the top 10 words, or all of them, whichever is smaller
    print(word_count[i])




'''   




print(string.punctuation)
purge = string.puntuation + "\n\t"

# loop over each word
# for word in words: #word creates a hold space for the loop itself but does not update the dictionary
for i in range(len(words)):
    # loop over each letter in word
    for char in words[i]:
        if char in string.punctuation:
            words[i] = words[i].replace(char, "")



# Print the most frequent top 10 out with their counts. You can do that with the code below.
# word_dict is a dictionary where the key is the word and the value is the count
word_dict = {'apples': 2, 'bananas': 1, 'pears': 1, 'kiwi': 7}
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])


'''

''' 
Notes below


# Read file
with open('data/phonebook.txt') as file:
    phonebook = file.read()

phonebook = phonebook.split('\n')
name = input("Lookup name: ")

found_entry = False
for entry in phonebook:
    if name.lower() in entry.lower():
        print(entry)
        found_entry = True

if not found_entry:
    print('No entry found.')
    name = input("Enter name for new entry: ")
    phone_number = input(f"Enter number for {name}: ")

    phonebook.append(name + " " + phone_number)

    phonebook.sort()
    with open('data/phonebook.txt', 'w') as file:
        file.write("\n".join(phonebook))

# How to remove characters
words = ["apple.", "@banana", "Kiwi", "can't", "keyboard!"]

import string
print(string.punctuation)

# .replace("!", "@")
# .replace("!", "")

purge = string.puntuation + "#\n\t"

# loop over each word
# for word in words: #word creates a hold space for the loop itself but does not update the dictionary
for i in range(len(words)):
    # loop over each letter in word
    for char in words[i]:
        if char in string.punctuation:
            words[i] = words[i].replace(char, "")



# How to add to dictionairy 
super_heros = {}
# {heronmae: 200}
while True:
    hero = input("enter a super hero")

    if hero in super_heros:
        super_heros[hero] += 1
    else:
# call dictionary 
        super_heros[hero] = 1

    print(super_heros)

'''