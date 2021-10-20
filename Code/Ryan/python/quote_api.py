# Quotes API
# For this lab we'll be using the Favqs Quotes API to first get a random quote, and then allow the user to find quotes by keyword. To accomplish this we'll be using the requests library.
# Version 1: Get a Random Quote
# The URL to get a random quote is https://favqs.com/api/qotd, send a request here, parse the JSON in the response into a python dictionary, and show the quote and the author.

import requests
# text = {}
# quote = {}
# quote_dict = {}
# author = {}
# url = 'https://favqs.com/api/qotd'

# request = requests.get(url)

# text = request.json()

# author = text['quote']['author']
# quote = text['quote']['body']

# Commented out to complete version 2
# print(f'Author: {author}')
# print(f'Quote: {quote}')

# Version 2: List Quotes by Keyword
# The Favqs Quote API also supports getting a list of quotes associated with a given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>. Prompt the user for a keyword, list the quotes you get in response, and prompt the user to either show the next page or enter a new keyword. You can use string concatenation to build the URL.
keyword_api_request = 'https://favqs.com/api/quotes/?page='

x = True
new_search_term = True
return_first_page = True
number_of_searches = 1
while x == True:
    if return_first_page == True:
        count = 1
        number = 1
    page = str(count)
    filters = '/&filter='

    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    # token = 'Authorization: Token token="YOUR_APP_TOKEN"'
    if new_search_term == True and number_of_searches == 1:
        keyword = input('Enter a keyword to search for quotes: ')
    number_of_quotes = 1
    # print(type(filters))
    # print(type(page))
    # print(type(keyword))

    keyword_search = keyword_api_request + page + filters + keyword

    request = requests.get(keyword_search, headers=headers)

    text = request.json()

    list_of_dict = []

    list_of_dict = text['quotes']


    for i in range(len(list_of_dict)):
        print('-'*75)
        print(f"Quote {number} for {keyword} is: {list_of_dict[i]['body']}")

        number += 1


    user_choice = input(f"\nPlease type\n'N' to show the next page,\n'D' for done, or \ntype another keyword to search for new quotes: ")
    if user_choice == 'N'or user_choice == 'n':
        count += 1
        number += 1
        new_search_term = False
        return_first_page = False
    elif user_choice == 'D' or user_choice == 'd':
        x = False
    else:
        return_first_page = True
        number_of_searches += 1
        keyword = user_choice




# quotes_on_this_page = []

# quotes_on_this_page = text['quotes']['body']

# print(text['quotes'])
# > enter a keyword to search for quotes: nature
# 25 quotes associated with nature - page 1
# <list of quotes>
# > enter 'next page' or 'done': next page
# 25 quotes associated with nature - page 2
# <list of quotes>
# > enter 'next page' or 'done': done
# > enter a keyword to search for quotes:

# This API endpoint requires an API key be included in a request header. You can find documentation of specifying request headers here and documentation on authorization with the Favqs API here under "Authorization".
# headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
# Other Quote APIs
# • Programming Quotes
# • Quotes Garden
#    • get random quote https://quote-garden.herokuapp.com/quotes/random
#    • get quotes by keyword https://quote-garden.herokuapp.com/quotes/search/<keyword/