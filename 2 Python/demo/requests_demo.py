import requests

# response = requests.get('https://api.chucknorris.io/jokes/random')

# Response code 
# print(response)

# Plain text
# print(response.text)

# Convert json to dictionary
# joke = response.json()
# print(joke)


# response = requests.get('https://api.chucknorris.io/jokes/categories')
# categories = response.json()

# for i in range(len(categories)):
#     print(i, categories[i])

# choice = int(input("Select a category: "))

# query = {
#     'category': categories[choice]
# }
# response = requests.get('https://api.chucknorris.io/jokes/random', params=query)
# print(response.text)

# options = {
#     'format': 'json',
#     'category': 'funny'
# }
# response = requests.get('https://api.ipify.org', params=options)

# ip = response.json()['ip']
# print(ip)

response = requests.get('https://www.gutenberg.org/cache/epub/66527/pg66654654527.txt')

if response.status_code == 200:
    print(response.text)
else:
    print("That book was not found")