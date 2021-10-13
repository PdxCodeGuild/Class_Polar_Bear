import string

book_index ={
}
#import book
with open('mobydick.txt', encoding='utf-8') as file:
    book = file.read()

#remove punctuation
for char in book:
    if char in string.punctuation:
        book = book.replace(char,'')

book=book.lower()

#split into list
word_list=book.split()

'''#Add items from list to dictionary
for item in word_list:
    if item in book_index:
        book_index[item]+=1
    else:
        book_index[item]=1'''

'''Optional 2'''

counter=1

for item in word_list:
    if counter < len(word_list):
        if item + ' ' + word_list[counter] in book_index:
            book_index[item + ' ' + word_list[counter]]+=1
        else:
            book_index[item + ' ' + word_list[counter]]=1
        counter+=1

#Find Top 10
'''words=list(book_index.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])'''

'''Optional 3'''
query=input('Enter a word to search for most frequently paired words: ')
pairs={}
for item in book_index:
    if query in item:
        pairs[item] =book_index[item]

words=list(pairs.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])