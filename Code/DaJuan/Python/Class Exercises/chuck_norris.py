import requests

response = requests.get('https://api.chucknorris.io/jokes/random')

# For response code use:
# print(response)

# Plain text:
# print(response.text)

# To convert into python dictionary, use .json() method:
joke = response.json()
# (Stored in variable for easier use)

# Get value
print(joke["value"])

'''Categories portion of exercise'''

# Make the request and store in variable
cat_response = requests.get('https://api.chucknorris.io/jokes/categories')
categories = cat_response.json()

# for statement lists all categories by number or [i]
for i in range(len(categories)):
    print(i, categories[i])

# input statement allows for user to choose number of category displayed
choice = int(input('Select a category: '))
cat_response = requests.get(f'https://api.chucknorris.io/jokes/random?category={categories[choice]}') #f statement
print(cat_response.text)


'''Query'''

# Query is dictionary of choices
query = {
    'categories': categories[choice]
}

# No need for f-string in link to connect input.  Insert params instead:
query_response = requests.get('https://api.chucknorris.io/jokes/random', params=query)