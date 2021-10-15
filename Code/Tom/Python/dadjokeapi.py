import requests

'''

Dad Joke API
Part 1

'''

'''api='https://icanhazdadjoke.com/'

headers={
    'Accept':'application/json'
}

response = requests.get(api, headers=headers)

data=response.json()
print(data['joke'])'''

'''

Dad Joke API
Part 2

'''

api_blank='https://icanhazdadjoke.com/search?term='


search=input('Search for jokes: ')

api=api_blank+search

headers={
    'Accept': 'application/json'
}

jokes=[]
response = requests.get(api, headers=headers)

data=response.json()

results=data['results']

counter=1
for joke in results:
    result=joke['joke']
    print(f'\n{counter} {result}')
    counter+=1