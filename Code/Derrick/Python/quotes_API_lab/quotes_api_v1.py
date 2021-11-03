import requests 

url = 'https://favqs.com/api/qotd'

response = requests.get(url)
data = response.json()
info = data['quote']

author = info['author']
quote = info['body']
msg = f'''Author: {author}
Quote: {quote}'''

print(msg)