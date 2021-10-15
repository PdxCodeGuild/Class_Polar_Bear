'''
___________________________________________________________________________
Project: Full Stack Evening Boot Camp - Python Lab 10 (Dad Joke API)
    Version: 1.0
Author: James Thornton
  Email: James.ed.thornton@gmail.com
Date: 14 OCT 2021
___________________________________________________________________________
'''

# Use the Dad Joke API to get a dad joke and display it to the user. 
# You may want to also use time.sleep to add suspense.
# Part 1
# Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ 
# with the accept header as application/json. This will return a dad joke in JSON format. 

import requests

url = 'https://icanhazdadjoke.com'

headers = {
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)

# You can then use the .json() method on the response to get a dictionary. 

data = response.json() # List of dictionaries
# print(data)

# Get the joke out of the dictionary and show it to the user.

print(data['joke'])

# Part 2
# Add the ability to "search" for jokes using another endpoint. 



# Create a REPL that allows one to enter a search term and go through jokes one at a time. 
# You can also add support for multiple pages.