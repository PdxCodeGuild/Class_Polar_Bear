import requests
from requests.api import head

def main(page=1, user_input=''):
    error = False
    url = f'https://favqs.com/api/quotes?page={page}&filter={user_input}'

    headers = {
        'Authorization':'Token token="855df50978dc9afd6bf86579913c9f8b"'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for i in range(len(data['quotes'])):
            total = 0
            total += i

        print(f"{total} quotes associated with {user_input} - page {data['page']}\n")

        if total != 0:
            for i in range(len(data['quotes'])):
                print(data['quotes'][i]['body'] + ' - ' + data['quotes'][i]['author_permalink'] + '\n')
        else:
            print('No more quotes available.')
            error = True
    else:
        print(f"Error {response.status_code}")

    return error
    

def second_input():
    next_or_done = input("Enter 'next page', 'new keyword', or 'done': ").lower()

    return next_or_done

url = 'https://favqs.com/api'

response = requests.get(url)

if response.status_code == 200:
    counter = 1
    first_input = input('Enter a keyword to search for quotes: ').lower()
    while True:
        error = main(page=counter, user_input=first_input)

        if error:
            break

        next_or_done = second_input()

        if next_or_done == 'next page':
            counter +=1
            continue
            
        elif next_or_done == 'new keyword':
            counter = 1
            first_input = input('Enter a keyword to search for quotes: ').lower()
            continue

        elif next_or_done == 'done':
            print("Have a good day. Goodbye")
            break
        
        else:
            print("Invalid entry, try again.")
            first_input = input('Enter a keyword to search for quotes: ').lower()

else:
    print(f'Error {response}')
