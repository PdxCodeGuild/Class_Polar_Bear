import requests

headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

def quotes(p, k):
    url = 'https://favqs.com/api/quotes?page=' + str(p) + '&filter=' + k
    response = requests.get(url, headers=headers)
    data = response.json()
    results = []
    for quote in data['quotes']:
        results.append(quote['author'] + quote['body'])
    return results

while True:
    page, x = 1, 0
    keyword = input("enter a keyword to search for quotes or 'exit': ")
    if keyword == 'exit':
        break

    while True:
        results = quotes(page, keyword)
        count = min(25, len(results)-x)
        print(f'{count} quotes associated with {keyword} - page {page}')
        for _ in range(count):
            print(results[x])
            x += 1

        if count < 25:
            print('no more pages')
            break

        action = input("enter 'next page' or 'done': ")
        if action == 'done':
            break
        page += 1

