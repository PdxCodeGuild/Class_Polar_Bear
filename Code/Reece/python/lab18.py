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
page = 1

url = 'https://favqs.com/api/quotes?page=<page>&filter=<keyword>'
# response = requests.get(url)

# json_data = json.loads(response.text)

# input_keyword = f'\nEnter a keyword to search for quotes: '
# for char in input_keyword:
#     print(char, end='', flush=True)
#     time.sleep(.06)
# keyword_choice = input('')
# keyword_choice = input('Enter keyword for quote search: ')
print(f'\n')

url = 'https://favqs.com/api/quotes?page=<page>&filter=<keyword>'

def search_function(pg, keyword):
    response = requests.get(url,headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params={'page':pg, 'filter':keyword})
    json_data = json.loads(response.text)
    return json_data

repeat = 'yes'

# input_keyword = input('Enter your search term: ')
# dad on page 1 gives many returns
# "amazing person" page 1 returns some, but far less
# "amazing person I know" page 1 returns one


# page = input('Enter a page number: ')
# data = search_function(page, input_keyword)
# quote_data = data['quotes']

# for quote_info in quote_data:
#     quote_author = quote_info['author']
#     quote_text = quote_info['body']
#     message = f"\n{quote_text}\n\t- {quote_author}"
#     for char in message:
#         print(char, end='', flush=True)
#         time.sleep(.01)
#     print(f"\n----------------------------------------------------\n")


# not 100% right at completing a new page...V

# while repeat == 'yes':
#     input_keyword = input('Enter your search term: ')
#     page = int(input('Enter a page number: '))
#     data = search_function(page, input_keyword)
#     if len(data) > 0:
#         quote_data = data['quotes']
#         for quote_info in quote_data:
#             quote_author = quote_info['author']
#             quote_text = quote_info['body']
#             message = f"\n{quote_text}\n\t- {quote_author}"
#             for char in message:
#                 print(char, end='', flush=True)
#                 time.sleep(.01)
#             print(f"\n----------------------------------------------------")
#         repeat = input('Enter "yes" to continue or git "enter" to exit: ')
#     else:
#         repeat = input('Enter "yes" to continue or git "enter" to exit: ')

while repeat == 'yes':
    input_keyword = input('Enter your search term: ')
    page = 1
    data = search_function(page, input_keyword)
    if len(data) > 0:
        quote_data = data['quotes']
        for quote_info in quote_data:
            quote_author = quote_info['author']
            quote_text = quote_info['body']
            message = f"\n{quote_text}\n\t- {quote_author}"
            for char in message:
                print(char, end='', flush=True)
                time.sleep(.01)
            print(f"\n----------------------------------------------------")
        next_page = ('Enter "next" to search for your keyword on the next page: ')
        if next_page == 'next':
            page += 1
            repeat = 'yes'
        else:
            repeat = input('Enter "yes" to continue or hit "enter" to exit: ')
    else:
        input_keyword = input('Enter your search term: ')
        repeat = input('Enter "yes" to continue or hit "enter" to exit: ')