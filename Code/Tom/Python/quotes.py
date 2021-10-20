import requests

headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
keyword='nature'
page_number=1
results=[]

def get_quote(pg,kw):
    api=f'https://favqs.com/api/quotes?page={pg}&filter={kw}'
    response = requests.get(api, headers=headers)
    data=response.json()
    counter=1
    for i in data['quotes']:
        author=i['author']
        qoute=i['body']
        results.append(f'\n{counter}. {qoute}\n{author}')
        counter+=1

def next_page(res):
    while True:
        nextpage=input(res)
        if nextpage.lower()=='next':
            return 'next'
        elif nextpage.lower()=='done':
            return 'done'
        else:
            print('Invalid reponse.')
            continue
keyword=input('Search quotes: ')
keyword=keyword.lower()
print(f'\n')

while True:
    page=str(page_number)
    get_quote(page,keyword)
    print(f'{len(results)} quotes associate with {keyword} - Page {page}.')
    
    for i in results:
        print(i)

    if len(results)<25:
        print(f'\nNo more Pages.')
        break
    else:
        user_next=next_page(f'\nPage {page}. Enter "next" or "done": ')
        if user_next=='next':
            print(f'\n')
            page_number+=1
            results=[]
        else:
            break