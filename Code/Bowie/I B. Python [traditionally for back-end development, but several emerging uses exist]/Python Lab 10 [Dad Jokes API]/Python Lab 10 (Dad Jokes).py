# ---------------- #
# Python Lab 10
# Dad Jokes API
# ---------------- #

import requests
import json

dad_jokes_api_url = "https://icanhazdadjoke.com/"
headers = {"accept": "application/json"}

def parse_joke_data(data):
    joke = data["joke"]
    print(f"Dad joke / Blague de papa: {joke}")

if __name__ == "__main__":
    resp = requests.get(dad_jokes_api_url, headers=headers)

    if resp.status_code == requests.codes.ok:
        parse_joke_data(json.loads(resp.text))
    else:
        print(f"Error getting dad joke... / Erreur lors de l'obtention de la blague de papa... [{resp.status_code}][{resp.reason}]: {resp.text}")

# ---------------- #