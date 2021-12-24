# ---------------- #
# Python Lab 13
# "Count Words"
# Revision to Remove "Trivial" Words
# Example from vintage edition of Gray's Anatomy
# 2021.12.21 [updated]
# ---------------- #

# using an early copy of Gray's Anatomy from archive.org:

import requests
response = requests.get('https://archive.org/stream/anatomyhumanbod00lewigoog/anatomyhumanbod00lewigoog_djvu.txt')
# set encoding to utf-8
response.encoding = 'utf-8' 

# print(response.text)

# convert to lower case
wordSet = response.text
wordSet = wordSet.lower()

# strip selected numbers and punctuation

def processStringCharacters(rawWordSet):
  otherCharacters = ".,;!?0123456789+-—^<>()[]{}§@" 
  for otherCharacter in otherCharacters:
    rawWordSet = rawWordSet.replace(otherCharacter, '')
  return(rawWordSet)


cleanData = processStringCharacters(wordSet)
# print(cleanData)

wordSet = response.text
commonWords = [" the ", " of ", "the ", 
" and ", " is ", " in ", " to ", " a ", " it ", 
" from ", " are ", " by ", " into ", " its ", 
" which ", " part ", " on " " with ", " or ", 
"of ", "with ", " with ", " as ", " at ", " two ",
" on ", " this ", " between ", "and "]

b = cleanData
for e in commonWords:
  b = b.replace(e," ")

# print(b)

# split into a list of words

wordList = b.split()
# print(wordList)
  
# dictionary  with words as keys and counts as values,
# if word is not in dictionary yet, add it with a count of 1
# if it is, increment its count

wordDictionary = dict.fromkeys(wordList, 1)
for word in wordList:
     if word in wordDictionary:
         wordDictionary[word] += 1
       
     else:
         wordDictionary[word] = 1

sorted_dictionary = {}
sorted_keys = sorted(wordDictionary, key = wordDictionary.get) 

for key in sorted_keys:
     sorted_dictionary[key] = wordDictionary[key]

# print the most frequent 10 out with their counts

dictionary_items = sorted_dictionary.items()

last_ten = list(dictionary_items)[-10:]

print(last_ten)

# # -------------- #