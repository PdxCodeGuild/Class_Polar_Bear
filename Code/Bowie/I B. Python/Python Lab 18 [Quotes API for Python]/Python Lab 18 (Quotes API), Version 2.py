# ---------------- #
# Python Lab 18
# Quoted API
# Version 2
# 2022.01.06
# ---------------- #
# The Favqs Quote API also supports getting a list of quotes associated with a given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>. 
# Prompt the user for a keyword, list the quotes you get in response, and prompt the user to either show the next page or enter a new keyword. You can 
# use string concatenation to build the URL.

# > enter a keyword to search for quotes: nature
# 25 quotes associated with nature - page 1
# <list of quotes>
# > enter 'next page' or 'done': next page
# 25 quotes associated with nature - page 2
# <list of quotes>
# > enter 'next page' or 'done': done
# > enter a keyword to search for quotes:
# This API endpoint requires an API key be included in a request header. You can find documentation of specifying request headers here and documentation on
# authorization with the Favqs API here under "Authorization".
# ---------------- #

import requests
import json

quotes_api_url = "https://favqs.com/api/quotes?page={page}&filter={keyword}"
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

page = 1
keyword = ""


def parse_quotes_data(data):
    quotes = data["quotes"]
    is_last_page= data["last_page"]

    if len(quotes) == 1 and quotes[0]["body"] == "No quotes found":
        raise Exception("No quotes found")
    else:
        quotes_list = [quote["body"] for quote in quotes]
        print(f"{len(quotes)} associated with {keyword} - page {page}:")
        print(quotes_list)
        if is_last_page:
            raise Exception("That is the last page! / C'est la derniere page !")


def parse_response(response):
    if response.status_code == requests.codes.ok:
        parse_quotes_data(json.loads(response.text))
    else:
        raise Exception(f"Error getting quotes [{response.status_code}][{response.reason}]: {response.text}")


def request_quotes():
    url = quotes_api_url.format(page=page, keyword=keyword)
    resp = requests.get(url, headers=headers)
    parse_response(resp)


if __name__ == "__main__":
    keyword = input("Please enter a keyword for search for quotes / Veuillez saisir un mot-cle pour obtenir les citations associees: ")

    try:
        request_quotes()
        command = input("\nEnter 'next page' or 'complete' / Entrez 'next page' ou 'complete' (...seulement en Anglais ici): ")
        while command != "complete":
            if command != "next page":
                command = input("Incorrect input; please, try again / Saisie incorrecte; veuillez essayer: ")
            else:
                page += 1
                request_quotes()
                command = input("\nEnter 'next page' or 'complete'/ Entrez 'next page' ou 'complete' (...seulement en Anglais ici):  ")
                
    except Exception as err:
        print(err)

# ---------------- #