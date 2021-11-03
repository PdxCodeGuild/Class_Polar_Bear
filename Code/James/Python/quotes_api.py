'''
___________________________________________________________________________
Project: Full Stack Evening Boot Camp - Python Lab 18 (Quotes API)
    Version: 1.0
Author: James Thornton
  Email: James.ed.thornton@gmail.com
Date: 18 OCT 2021
___________________________________________________________________________
'''

# The URL to get a random quote is https://favqs.com/api/qotd, 
# send a request here, 

import requests

url = 'https://favqs.com/api/qotd'

headers = {
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)

# parse the JSON in the response into a python dictionary, 

data = response.json()

# and show the quote and the author.

print(data['quote']['body'])
print('by')
print(data['quote']['author'])

