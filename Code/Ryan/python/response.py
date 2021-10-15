import requests

url = 'https://ghibliapi.herokuapp.com/films'

headers ={
    'Accept': 'application/json'
}
#params= #this will pass in a visible querry data
response = requests.get(url, headers=headers) #this needs a dictionary inline or outside #params can go here as well for querries)

#converst json into python
data = response.json() #list of dictionsaires

#prints the first film title from data dict
print(data[0]['title'])

for film in data:      #iterate over list, call each dictionary 'film'
    print(film['release_date'], film['title'])
    print(film['description'])
    print('-'*50)

