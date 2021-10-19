import requests
import random


##### Version 1 - Get a random quote #####
url = 'https://favqs.com/api/qotd'

response = requests.get(url)
response = response.json()

rand_quote = response['quote']['body']
author = response['quote']['author']
# print(rand_quote, ' -', author)

##### Version 2 - List Quotes by keyword #####
url = 'https://favqs.com/api/quotes?page=1&filter=nature'
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

# response = requests.get(url, headers=headers)

# print(response.status_code)

user_keyword = input('Enter a keyword: ')
page = 0

while True:
  page += 1
  i = 0
  response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={user_keyword}', headers=headers).json()
  if response['last_page']:
    print('\nNo more pages!')
    another_keyword = input('\nEnter another keyword, or press enter to finish: ')
    if another_keyword == '':
      print('Goodbye')
      break
    else:
      page = 0
      user_keyword = another_keyword
      continue
  else:
    quotes = response['quotes']
    quotes_length = len(response['quotes'])
    page_num = response['page']
    if page_num == 1:
      print(f'\n\n{quotes_length} quotes associated with {user_keyword} - page {page_num}\n')
    else:
      print(f'\n\n{quotes_length} more quote(s) associated with {user_keyword} - page {page_num}\n')
    for quote in quotes:
      i += 1
      print(f"{i}. {quote['body']} -{quote['author']}")
  next_page = input('\nEnter "done or d" if finished, or enter for next page: ').lower()
  if next_page == 'done' or next_page == 'd':
    print('Goodbye')
    break
  else:
    continue
