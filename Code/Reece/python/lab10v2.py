import requests
import time

# Version 1 -------------------------------------------------------------------------------------#

# url = 'https://icanhazdadjoke.com/'
# response = requests.get(url,headers={'Accept': 'application/json'})
# data = response.json()
# message = data['joke']
# print(f"\n")
# for char in message:
#     print(char, end='', flush=True)
#     time.sleep(.01)
# print(f"\n")

# Version 2 -------------------------------------------------------------------------------------#

url = 'https://icanhazdadjoke.com/search'

choice = input('Enter a search term: ')

response = requests.get(url,headers={'Accept': 'application/json'}, params=choice)

data = response.json()

print(f'\n')
for i in data['results']:
    message = i['joke']
    for char in message:
        print(char, end='', flush=True)
        time.sleep(.01)
    print(f"\n")