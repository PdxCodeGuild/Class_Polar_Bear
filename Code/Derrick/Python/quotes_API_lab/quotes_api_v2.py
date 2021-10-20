import requests 

url = 'https://favqs.com/api/quotes'

headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

def get_url(u,page=1,options={}):

    options['page'] = page
    options['filter'] = search 
    response = requests.get(u,params=options,headers=headers) 
    data = response.json()
    quotes = data['quotes']
    # Ask for new search term if no quotes are found in the body key/value pair
    if quotes[0]['body'] == 'No quotes found': 
        print('No quotes found.')
        return False
    
    print('Page: ' + str(data['page']) + '\nQuotes:') 
    
    for quote in quotes: 
        print(quote['body'])
    
   
while True:

    search = input('Search for a quote: ') 
    page_num = 1 
    has_quotes = get_url(url,page_num) 

    if has_quotes == False:
            continue
    # check if user wants to continue to next page
    while True: 
        next_page = input('Please enter \'next page\' or \'done\': ')
        
        if next_page == 'done' or next_page != 'next page':
            break

        page_num += 1
        has_quotes = get_url(url,page_num)

        if has_quotes == False:
            break
        
            