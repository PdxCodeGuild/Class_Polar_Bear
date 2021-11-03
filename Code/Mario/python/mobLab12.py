# Tom, DaJuan, Aaron, Gabe, Bowie

# The API endpoint https://api.adviceslip.com/advice will return a random advice slip.
# Send a request to this URL and display the advice given in response.

# Another endpoint https://api.adviceslip.com/advice/search/{query} will allow you to search advice slips.
# Prompt the user for a term to search with, put that string into the URL, send the request, and display the results.

import requests

# PART ONE
# url = 'https://api.adviceslip.com/advice'

# response = requests.get(url)
# data = response.json()
# print(data['slip']['advice'])

# PART TWO


def api(search):
    url = f'https://api.adviceslip.com/advice/search/{search}'
    response = requests.get(url)
    data = response.json()
    slips = data['slips']
    counter = 1
    for advice in slips:
        slips = advice['advice']
        print(f"{counter}: {slips}\n")
        counter += 1


api(input("What would you like to search: "))
