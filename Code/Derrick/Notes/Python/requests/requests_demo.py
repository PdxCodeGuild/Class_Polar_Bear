import requests 

# response = requests.get('https://api.chucknorris.io/jokes/categories')
# categories = response.json()

# for i in range(len(categories)):
#     print(i,categories[i])

options = {
    'format': 'json'
}

response = requests.get('https://api.ipify.org', params=options)
response = response.json()
print(response['ip'])


