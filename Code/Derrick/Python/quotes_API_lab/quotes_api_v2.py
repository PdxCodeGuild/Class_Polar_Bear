import requests 

url = 'https://favqs.com/api/quotes'

headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

def get_url(u,page=1,options={}):

    # vars
    options['page'] = page
    options['filter'] = search 
    response = requests.get(u,params=options,headers=headers) 
    data = response.json()
    quotes = data['quotes']

    # Ask for new search term if no quotes are found in the body key/value pair
    if quotes[0]['body'] == 'No quotes found':
        print('No quotes found.')
        return False

    # Make output look nicer and add current page number
    print('Page: ' + str(data['page']) + '\nQuotes:')

    # print quotes
    for quote in quotes:
        print(quote['body'])
    
    
while True:

    # ask for search term
    search = input('Search for a quote: ')
    
    # set page num equal to 1 to reset page parameter for new search
    page_num = 1

    # Check if quotes exist for search term, if not go to top of loop and reprompt for search term
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
        
            
    


