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

def v_2_dict(list):
    dictionary = {}
    for i in range(len(list) -1):
        pair = list[i] + " " + list[i+1]
        if pair in dictionary:
            dictionary[pair] += 1
        else:
            dictionary[pair] = 1
    
    return dictionary

def most_freq_word(user_word, list):
    following_word = ""
    for i in range(len(list)):
        if list[i] == user_word:
            following_word = list[i + 1]

    return following_word

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

    # we call our function for version 2 
    v2_book_dict = v_2_dict(book_list)

    # unordered list for v3
    unordered_list = book_list

    # sort list
    book_list.sort()

    # call function to convert list into dictionary
    book_dict = convert(book_list)
    

    print('Top 10 words')

    # book_dict is a dictionary where the key is the word and the value is the count
    words = list(book_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])

    print()

    print('Top 10 word pairs')

    # version 2:
    # Count how often each unique pair of words is used, 
    # then print the top 10 most common pairs with their counts.
    # book_dict is a dictionary where the key is the word and the value is the count
    words_v2 = list(v2_book_dict.items()) # .items() returns a list of tuples
    words_v2.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words_v2))):  # print the top 10 words_v2, or all of them, whichever is smaller
        print(words_v2[i])

    
    print()

    # version 3:
    # Let the user enter a word, then show the words which most frequently follow it.
    while True:
        user_word = input("Enter a word: ").lower()

        following_word = most_freq_word(user_word, unordered_list)
        print(following_word)
        if following_word == None:
            continue
        else:
            print(f"The most frequently word after '{user_word}'' is '{following_word}'")
            break
