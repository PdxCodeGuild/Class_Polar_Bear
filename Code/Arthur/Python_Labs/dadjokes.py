'''
Dad Joke API
Use the Dad Joke API to get a dad joke and display it to the user. 
You may want to also use time.sleep to add suspense.
Part 1
Use the <../docs/16%20Requests.md|requests> library to send an 
HTTP request to https://icanhazdadjoke.com/ with the accept header as 
application/json. This will return a dad joke in JSON format. 
You can then use the .json() method on the response to get a dictionary. 
Get the joke out of the dictionary and show it to the user.
Part 2 (optional)
Add the ability to "search" for jokes using another endpoint. Create a REPL that allows one to enter a search term and go through jokes one at a time. You can also add support for multiple pages.

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

dad jokes api


'''
import requests

headers ={
  'Accept':'application/json'
}

url ='https://icanhazdadjoke.com/'

response = requests.get(url, headers = headers)

print(response.json())

