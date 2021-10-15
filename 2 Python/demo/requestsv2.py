import requests

url = 'https://ghibliapi.herokuapp.com/films'

headers = {
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)

data = response.json() # List of dictionaries

# print(data[0]['title'])

for film in data:      # Iterate over list, call each dictionary 'film'
    print(film['title'], film['release_date'], film['description'])
    print('-'*50)
