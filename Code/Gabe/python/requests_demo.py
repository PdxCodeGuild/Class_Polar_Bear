import requests
from requests.models import Response

# response = requests.get('https://api.chucknorris.io/jokes/random')

# Response code
# print(response)

# Plain text
# print(response.text)

# Convert JSON into a python dictionary using .json()
# joke = response.json()
# print(joke['value'])

########################################################################
# response = requests.get('https://api.chucknorris.io/jokes/categories')
# # print(response.json())

# categories = response.json()

# for i in range(len(categories)):
#   print(i, ': ', categories[i])

# choice = input('Select a category: ')

# query = categories[int(choice)]
# response = requests.get(f'https://api.chucknorris.io/jokes/random', params=query)
# response = response.json()

# print(
#   f'''
#   Your category is: {categories[int(choice)]}
#   Joke: {response['value']}
#   '''
# )
###########################################################################

# options = {
#   'format': 'json'
# }

# response = requests.get('https://api.ipify.org', params=options)

# # print(response.text)

# ip = response.json()['ip']

# print(ip)

#############################################################################

response = requests.get('https://www.gutenberg.org/cache/epub/66527/pg66527.txt')

if response.status_code == 200:
  print(response.text)
else:
  print('That book was not found')