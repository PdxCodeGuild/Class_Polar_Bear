import string

book_index ={
}

#import book
with open('mobydick.txt', encoding='utf-8') as file:
    book = file.read()
#print(book)
#remove punctuation
for char in book:
    if char in string.punctuation:
        book = book.replace(char,'')
book=book.lower()

#split into list
word_list=book.split(' ')

#Add items from list to dictionary
for item in word_list:
    if item in book_index:
        book_index[item]+=1
    else:
        book_index[item]=1

#Find Top 10
words=list(book_index.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])