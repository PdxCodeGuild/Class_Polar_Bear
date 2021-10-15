import requests 

url = 'https://ghibliapi.herokuapp.com/films'

response = requests.get(url) 
lst = response.json()

for i in lst:
    print('Title: ' + i['title'] + ' (' + i['release_date'] + ')\n' + 'Description: ' + i['description'] + '\n')
