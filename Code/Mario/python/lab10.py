import requests
import os
import time


def clear(): return os.system('cls')


headers = {
    'Accept': 'application/json',
}

search = input("Enter a search term: ")
see_more = True

response = requests .get(f"https://icanhazdadjoke.com/search?term={search}",
                         headers=headers, params="dog").json()['results']
# print(response)
for i in range(len(response)):
    joke = response[i]['joke']
    clear()
    if see_more:
        time.sleep(.3)
        print(f"{joke}\n")
        time.sleep(3)
        show_another_joke = input(
            f"Would you like to see another one?\ny/n ? ")
        see_more = True if show_another_joke == 'y' else False
    else:
        break
