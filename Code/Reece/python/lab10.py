import requests
import time

url = 'https://icanhazdadjoke.com/'

response = requests.get(url,headers={'Accept': 'application/json'})

data = response.json()

message = data['joke']
print(f"\n")
for char in message:
    print(char, end='', flush=True)
    time.sleep(.01)
print(f"\n")