'''Lab 15: Count Words
Let's write a python module to analyze a given text file containing a
 book for its vocabulary frequency and display the most frequent words to
the user in the terminal. Remember there isn't any "perfect" way to identify
a word in english (acronymns, mr/ms, contractions, etc), try to find rules that
 work best.

Find a book on Project Gutenberg and navigate to the plain-text version. 
You can then send a request to that url using the requests library to get 
the text into Python. You can also save the file into the same folder as the .py
 file and open it using with.

import requests
response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
print(response.text)
We can also download a file of english words and place it next our .py 
file and load it like so:

with open('the_raven.txt', 'r', encoding='utf-8') as file:
    text = file.read()
print(text)
Take the following steps to build up our dictionary. 
The result should look something like {'a': 3, 'the': 4}

Make everything lowercase, strip punctuation, split into a list of words.
Your dictionary will have words as keys and counts as values. If a word isn't in 
your dictionary yet, add it with a count of 1. If it is, increment its count.
Print the most frequent top 10 out with their counts. You can do that with the code
 below.
# word_dict is a dictionary where the key is the word and the value is the
#  count
word_dict = {'apples': 2, 'bananas': 1, 'pears': 1, 'kiwi': 7}
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, 
based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them,
     whichever is smaller
    print(words[i])'''

#using string.punctuation

# import string

# words = ["apple.", "@banana", "Kiwi  ", "can't", "keyboard!", "?what", "the\ncat"]

# # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# print(string.punctuation)

# purge = string.punctuation + "\n"

# for i in range(len(words)):
#     for char in words[i]:
#         if char in purge:
#             words[i] = words[i].replace(char, "")
#     print(words[i])
# print(words)
# while True:
#     hero =input("enter a hearo")
#     if hero in superhero:
#         superhero[hero] +=1
#     else:
#         superhero[hero]=1
#     superhero[hero]=1


    # with open('Curtisaviation.txt','w',encoding='utf-8') as file :
# dictionary_name[key] = value
#examples used 
# scones = {
# 	"Fruit": 22,
# 	"Plain": 14,
# 	"Cinnamon": 4,
# 	"Cheese": 21
# }

# scones["Cherry"] = 10

# print(scones)


# with open('countwords.txt','w',encoding='utf-8') as file:
#     text1 = file.write(f"{word}:{adding_count}")
# superhero ={

# }
import string
word_dict = {}
# open the file for reading , you don't need to add the parameter R
with open('Curtisaviation.txt','r',encoding='utf-8') as file:
    text = file.read()
    #print the first 1000 characters
    # print(text[:1000])

#Make everything lowercase, strip punctuation, split into a list of words.
text =text.lower()
#removing punctuation
# text=text.strip('!?;.:[],')
purge = string.punctuation + "\n""" + string.digits
# print(purge)

for i in range (len(text)):
    for char in text[i]:
        if char in purge:
            text[i]=text[i].replace(char,"")
        text =text[i].join(text.split('\n'))

text =text.replace("  ","")
print(text)
      
        
    # print(text[i].join(text.split('\n')) ) 
        # print(text)
   
        # text=text.split('\n')
         # print(text)

        # word = input("word lookup: ")

        # found_entry = False

        # for entry in text :
        #     if word.lower() in entry.lower():
        #         word_dict[word]+=1
        #         print(entry)
        #         found_entry = False  

        # if not found_entry:
        #      print("file not found")
        #      word = input(f"Enter word for new entry : ")
        #         # adding_count = input(f"Enter count for {word}: ")
        # word_dict[word]=1
        # print(word_dict)
    

''''
alternative 
afte with open

purge = string.punctuation +  string.digits + '\n ""':

for char in purge :
    if char in text:
        text = text.replace(char,"")
text = text.replace(" ","")
text = text.split('')

dictionary
word_count ={}
for i in range(len(text)):
    current_word = text[i]
    if current_word in word_count:
        word_count[current_word] +=1
    else :
        word_count[current_word] = 1
word =list(word_count.items())
words.sort(key=lambad tup:tup[1], reverse = true)
for i in range(min(19,len(words))):
    print(words[i])


version2
print(text)
dictionary
word_count ={}
for i in range(len(text)-1):
    current_word = text[i]
    next_word = text[i+1]
    pair = current_word + " " + next_word
    if pair in word_count:
        word_count[pair] +=1
    else :
        word_count[pair] = 1
word =list(word_count.items())
words.sort(key=lambad tup:tup[1], reverse = true)
for i in range(min(19,len(words))):
    print(words[i])

version3
do as home work

'''