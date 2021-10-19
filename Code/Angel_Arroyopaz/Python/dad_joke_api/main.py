import requests
import time
import string

# v1

# headers = {
#     'Accept': 'application/json'
# }

# url = 'https://icanhazdadjoke.com'

# response = requests.get(url, headers=headers)

# data = response.json()

# if response.status_code == 200:
#     print(data['joke'])

# else:
#     print(f'Error {response.status_code}')



# v2

def loop(list):
    for i in range(len(list)):
        print(i+1, "-", list[i]['joke'])
        print("Fetching...")
        time.sleep(5)

url = 'https://icanhazdadjoke.com/search'

response = requests.get(url)

if response.status_code == 200:
    while True:
        user_input = input('Enter a word: ')
        not_letters = string.digits + string.punctuation

        valid = True
        for i in range(len(user_input)):
            if user_input[i] in not_letters:
                valid = False

        if valid == False:
            print('Invalid entry. Try again.')
            continue
        
        else:
            break


    
    headers = {
        'Accept': 'application/json'
    }

    query = {
        'term': user_input
    }

    response = requests.get(url, headers=headers, params=query)

    data = response.json() # dictionary of lists

    if data['current_page'] == 1:
        jokes = data['results'] # list of dictionaries
        if jokes == []:
            print('Sorry no jokes found.')
        else:
            loop(jokes)
            
    elif data['current_page'] == 2:
        jokes = data['results'] # list of dictionaries
        loop(jokes)

    elif data['current_page'] == 3:
        jokes = data['results'] # list of dictionaries
        loop(jokes)


            

else:
    print(f'Error {response.status_code}')