'''
___________________________________________________________________________
Project: Full Stack Evening Boot Camp - Python Lab 18 (Quotes API)
    Version: 2.0
Author: James Thornton
  Email: James.ed.thornton@gmail.com
Date: 18 OCT 2021
___________________________________________________________________________
'''

# The Favqs Quote API also supports getting a list of quotes associated with a given 
# keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>. 
# Prompt the user for a keyword, list the quotes you get in response, 
# and prompt the user to either show the next page or enter a new keyword. 
# You can use string concatenation to build the URL.

import requests
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}


while True:
  page = 1 
  keyword = input("Enter a string you would like to see in a quote or done to quit: ")
  url = 'https://favqs.com/api/quotes?page=' + str(page) + '&filter=' + keyword
  response = requests.get(url, headers=headers)
  data = response.json()
  if keyword == 'done':
    break
  else:
    while True:
      count = 0
      url = 'https://favqs.com/api/quotes?page=' + str(page) + '&filter=' + keyword
      response = requests.get(url, headers=headers)
      data = response.json()
      for quote in data['quotes']:
        print(quote['body'])
        print('by')
        print(quote['author'])
        count += 1
      print(f'{count} quotes associated with keyword in page {page}')
      page += 1 
      next = input('Enter \'next page\' or \'done\': ')
      if next == 'done':
        break

# print(data['quotes'][1]['body']) This prints quotes


