import requests

url = 'https://favqs.com/api/quotes?page=1&filter=bird'

headers = {
    
    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
 
    }


keyword = input("Enter a keyword to search for quotes: ")
page = 0

while True:
    page += 1
    line_number = 0
    response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}', headers=headers).json()
    if response['last_page']:
        print('No More Quotes!')
        new_keyword = input('Enter a new keyword, or press Enter to quit')
        if new_keyword == '':
            print('Have a nice day!')
            break
        page = 0
        keyword = new_keyword
        continue
    else:
        quotes = response['quotes']
        number = len(response['quotes'])
        page_number = response['page']
        if page_number == 1:
            print(f'{number} quotes associated with {keyword}')
        else:
            print(f'{number} more quote(s) associated with {keyword} - page {page_number}')
        for quote in quotes:
            line_number += 1
            print(f"{line_number}. {quote['body']} -{quote['author']}")
    next_page = input('Enter Done if finished, or press Enter for next page: ').lower()
    if next_page == 'done':
        print('Have a nice day!')
        break
    else:
        continue







