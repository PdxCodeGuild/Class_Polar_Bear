import requests 
import time 

url = 'https://icanhazdadjoke.com/search'

dataType = {
    'Accept': 'application/json'
}

queries = {
        # 'limit': 1
}

while True:
    yesOrNo = input('Would you like to hear a Dad joke?(yes/no) ')

    if yesOrNo.lower() == 'no':
        break

    userInput = input('Search for a dad joke: ')
    queries['term'] = userInput
    data = requests.get(url,headers=dataType,params=queries).json()

    if data['results'] == []:
            print('No joke found...')
    
    for i in data['results']:
         
        try:
            print('Fetching joke....')
            time.sleep(2)
            print(i['joke'])
            time.sleep(2)
            again = input(f'Would you like to hear another one related to {userInput}?')

            if again.lower() == 'no':
                break  

        except IndexError:
            print('No joke found')

        

