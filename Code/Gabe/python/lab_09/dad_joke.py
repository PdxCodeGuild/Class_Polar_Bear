import requests, time

# url = 'https://icanhazdadjoke.com/'

headers = {
  'Accept': 'application/json'
}

# response = requests.get(url, headers=headers)

# dad_joke = response.json()['joke']

# for i in range(3):
#   print('\nWait for it.', end='.'), time.sleep(1), print('..')
#   time.sleep(.5)

# print(f'\n{dad_joke} ')

# response = requests.get(f'https://icanhazdadjoke.com/search?term=&page=2', headers=headers)

# jokes_list = response.json()

# print(jokes_list)



term = input('Enter a search term: ')
page = 0
while True:
  page += 1
  response = requests.get(f'https://icanhazdadjoke.com/search?term={term}&page={page}', headers=headers)
  searched_list = response.json()['results']
  if len(searched_list) == 0:
    again = input('No more pages, search again? y/n: ').lower()
    if again =='y' or again == 'yes':
      page = 0
      term = input('\nEnter search term: ')
      continue
    else:
      break
  for joke in searched_list:
    current_joke = joke['joke']
    print(f'\n{current_joke}')
    choice = input('\nType "y" to choose joke, to continue press enter: ').lower()
    if choice == 'y':
      print(
      f'''
      Your Joke is:
      {current_joke}
      '''
      )
      break
  next_page = input('Go to next page? y/n: ').lower()
  if next_page == 'y' or next_page == 'yes':
    continue
  else:
    break


# print(current_joke)
