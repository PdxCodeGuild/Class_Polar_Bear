import requests

url = 'https://favqs.com/api/qotd'

headers = {
    
    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
 
    }

response = requests.get(url, headers=headers)



data = response.json()

print(data['quote'].get('body'))
print('     -',data['quote'].get('author'))


