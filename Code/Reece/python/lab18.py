# Reece Adams - Lab18.py - lab 18 - Quotes API #

from types import NoneType
import requests
import json
import time

# Version 1 #

# url = 'https://favqs.com/api/qotd'
# response = requests.get(url)

# json_data = json.loads(response.text)

# message = (f"{json_data['quote']['body']}\n\t- {json_data['quote']['author']}\n")

# print(f'\n')
# for char in message:
#     print(char, end='', flush=True)
#     time.sleep(.06)
# print(f"\n")

# Version 2 #
url = 'https://favqs.com/api/quotes?page=<page>&filter=<keyword>'

def search_function(pg, keyword):
    response = requests.get(url,headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params={'page':pg, 'filter':keyword})
    json_data = json.loads(response.text)
    return json_data

repeat = 'yes'

counter = 0
while repeat == 'yes':
    if counter == 0:
        input_keyword = input('Enter your search term: ')
        counter += 1
        page = int(input('Enter a page number: '))
    elif counter > 0:
        same_keyword = input(f'\nDo you want to search "{input_keyword}" on next page? If so type "yes": ')
        if same_keyword == 'yes':
            page += 1
    data = search_function(page, input_keyword)
    quote_body = data['quotes'][0]['body']
    if quote_body != 'No quotes found':
        quote_data = data['quotes']
        for quote_info in quote_data:
            quote_author = quote_info['author']
            quote_text = quote_info['body']
            message = f"\n{quote_text}\n\t- {quote_author}\n"
            for char in message:
                print(char, end='', flush=True)
                time.sleep(.01)
        print(f"\n- Page {page} ---------------------------------------------------- Page {page} -\n")
    else:
        repeat = input(f'\nNo data found for page {page}...\n\nType "yes" keep going or hit "enter" to exit: ')