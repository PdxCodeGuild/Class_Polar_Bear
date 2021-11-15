import requests

response = requests.get('https://favqs.com/api/qotd', params = {'format': 'json'})
print(response.text) # 76.105.187.182
data = response.json()
print(data)

import json

url = 