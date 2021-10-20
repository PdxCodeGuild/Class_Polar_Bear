import requests

url = 'https://favqs.com/api/qotd'

response = requests.get(url)

data = response.json()

if response.status_code == 200:
    print(data['quote']['body'] + '\n' + data['quote']['author'])
else:
    print(f'Error {response}')