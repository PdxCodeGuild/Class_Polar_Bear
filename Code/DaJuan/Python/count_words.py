import requests
import string

symbols = string.punctuation

response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
response.encoding = 'utf-8'
#print(response.text)
words = response.json()

word_dict = {}

plain_text = words.read().lower().strip()
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