import requests 

# url = 'https://api.adviceslip.com/advice' 


queries = {}
userInput = input('Search advice: ')
url = f'https://api.adviceslip.com/advice/search/{userInput}'
response = requests.get(url)

data = response.json()

# for advice in data['slips']:
#     print(advice['advice'])



print(data)