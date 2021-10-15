import requests 

url = 'https://icanhazdadjoke.com/search'

dataType = {
    'Accept': 'application/json'
}

queries = {
        'limit': 1
}

while True:
    yesOrNo = input('Would you like to hear a Dad joke?(yes/no) ')

    if yesOrNo.lower() == 'no':
        break

    userInput = input('Search for a dad joke: ')
    queries['term'] = userInput
    data = requests.get(url,headers=dataType,params=queries).json()

    try:
        print(data['results'][0]['joke'])
    except IndexError:
        print('No joke found')

