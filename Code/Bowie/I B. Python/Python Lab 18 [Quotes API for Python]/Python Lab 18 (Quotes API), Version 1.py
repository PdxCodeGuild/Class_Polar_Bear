# ---------------- #
# Python Lab 18
# Quoted API
# Version 1
# 2022.01.06
# ---------------- #

# Version 1: Get a Random Quote
# The URL to get a random quote is https://favqs.com/api/qotd, send a request here, 
# parse the JSON in the response into a python dictionary, and show the quote and the author.
# ---------------- #

import requests
import json

quotes_api_url = "https://favqs.com/api/qotd"

def parse_quotes_data(data):
    quote = data["quote"]
    print(f"Author / Auteur: {quote['author']}\nQuote / Citation: {quote['body']}")

if __name__ == "__main__":
    print("The program is getting a random quote... / Le programme est en train d'obtenir une citation aleatoire...\n")
    resp = requests.get(quotes_api_url)

    if resp.status_code == requests.codes.ok:
        parse_quotes_data(json.loads(resp.text))
    else:
        print(f"There was an error. / Il y avait une erreur. [{resp.status_code}][{resp.reason}]: {resp.text}")

# ---------------- #