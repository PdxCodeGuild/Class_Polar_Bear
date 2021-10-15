# Dad Joke API
# Use the Dad Joke API to get a dad joke and display it to the user. You may want to also use time.sleep to add suspense.

# Part 1
# Use the <../docs/16%20Requests.md|requests> library to send an HTTP request to https://icanhazdadjoke.com/ with the accept header as application/json. This will return a dad joke in JSON format. You can then use the .json() method on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.


import requests
import time
url = 'https://icanhazdadjoke.com/'

headers ={
    'Accept': 'application/json'
}

# paramater = {

# }

response = requests.get(url, headers=headers)
punctuation = ['.', '?', '!']
sentence = 0
joke_dict = response.json()
start_sentence = 0

joke_only = joke_dict['joke'].split(' ')

for word in range(len(joke_only)):
    for char in joke_only[word]:
        if char in punctuation and sentence != 1:
            end_sentence = word + 1
            print(' '.join([joke_only[i] for i in range(end_sentence)]))
            sentence = 1
            start_sentence = word + 1
            time.sleep(3)
            continue

print(' '.join([joke_only[i] for i in range(start_sentence, len(joke_only))]))




# Part 2 (optional)
# Add the ability to "search" for jokes using another endpoint. Create a REPL that allows one to enter a search term and go through jokes one at a time. You can also add support for multiple pages.

'''
Search for dad jokes
GET https://icanhazdadjoke.com/search - search for dad jokes.

This endpoint accepts the following optional query string parameters:

page - which page of results to fetch (default: 1)
limit - number of results to return per page (default: 20) (max: 30)
term - search term to use (default: list all jokes)
Receive search results back as JSON:

$ curl -H "Accept: application/json" https://icanhazdadjoke.com/search
{
  "current_page": 1,
  "limit": 20,
  "next_page": 2,
  "previous_page": 1,
  "results": [
    {
      "id": "M7wPC5wPKBd",
      "joke": "Did you hear the one about the guy with the broken hearing aid? Neither did he."
    },
    {
      "id": "MRZ0LJtHQCd",
      "joke": "What do you call a fly without wings? A walk."
    },
    ...
    {
      "id": "usrcaMuszd",
      "joke": "What's the worst thing about ancient history class? The teachers tend to Babylon."
    }
  ],
  "search_term": "",
  "status": 200,
  "total_jokes": 307,
  "total_pages": 15
}

'''