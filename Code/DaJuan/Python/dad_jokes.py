import requests


url = 'https://icanhazdadjoke.com/'

query = {
    'Accept':'application/json'
}

response = requests.get(url,headers=query)
joke = response.json()['joke']

while True:
    question = input('Do you want to hear a bad Dad joke?(Y/N) ')

    if question.upper() == 'N':
        break
    else:
       print(joke) 


