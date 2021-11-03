import requests


'''
Part 1
The API endpoint https://api.adviceslip.com/advice will return a random advice slip. Send a request to this URL and display the advice given in response.
'''
response = requests.get('https://api.adviceslip.com/advice')

# print(response.json())


'''
Part 2
Another endpoint https://api.adviceslip.com/advice/search/{query} will allow you to search advice slips.
Prompt the user for a term to search with, put that string into the URL, send the request, and display the results.
'''

response = requests.get(f'https://api.adviceslip.com/advice/search/joy')

print(response.text)