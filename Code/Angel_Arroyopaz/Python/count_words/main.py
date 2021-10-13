import string

# function to convert list to dictionary and increment value of repeted words
def convert(list):
    dictionary = {}
    for i in range(len(list)):
        if list[i] in dictionary:
            dictionary[list[i]] += 1
        else:
          dictionary[list[i]] = 1

    return dictionary

punctuation = string.punctuation + string.digits + "——————————" + "◆⁴"

# open file
with open('book.txt') as file:
    text = file.read().lower()

    # loop through string to find and remove items in punctuation variable
    for i in text:
        if i in punctuation:
            text = text.replace(i, "")

    # split words and turn string into a list
    book_list = text.split()

    # sort list
    book_list.sort()

    # call function to convert list into dictionary
    book_dict = convert(book_list)

    # word_dict is a dictionary where the key is the word and the value is the count
    word_dict = book_dict
    words = list(word_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])

    # print(book_dict)
