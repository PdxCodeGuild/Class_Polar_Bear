# Lists are index: value pairs
# Dictionaries are key: value pairs

person = {
  'first_name': 'Brad',
  'last_name': 'Doe',
  'age': '47'
  }

# add a new property
person['favorite_color'] = 'red'
person['favorite_color'] = 'blue'

person['first_name'] = 'John'

person['pet_name'] = 'rocky'

# Looking if a key exists - use second perameter as message
# print(person.get('nickname', 'No nickname found'))

nickname = person.get('nickname', False)

# if nickname:
#   print(f"{person['first_name']}\'s nickname is {nickname}")
# else:
#   print(f"{person['first_name']} has no nickname")


# Delete a key value

del person['pet_name']

person['fave_operating_system'] = 'MacOS'

# 'in' keyword looks to see if key is in dict
# if 'fave_food' in person:
#   print(f"{person['first_name']}'s favorite food is {person['fave_fruit']}")
# elif 'fave_operating_system' in person:
#   print(f"{person['first_name']}'s favorite OS is {person['fave_operating_system']}")

# print(person)

colors = ['red', 'blue', 'yellow']

# for color in colors:
  # print(color)

# for key in person:
#   if key == 'first_name':
    # print('This is a real person')


# Create a user login system, use dictionary to store username: password
accounts = {
  'batman': 'notbrucewayne1'
}

while True:
  choice = input('select (1) to sign up, (2) to login, (3) Quit: ')
  if choice == '1':
    # Sign up a new user (username cannot ve taken)
    username = input('Enter a username: ')
    password = input('Enter a passowrd: ')
    if username in accounts:
      print('username already exists...')
      continue
    else:
      accounts[username] = password
  elif choice == '2':
    # Login user
    username = input('Enter a username: ')
    password = input('Enter a passowrd: ')

    # None != 'None'
    if accounts.get(username, None) == password:
      print(f'Welcome {username}')
    else:
      print(f"username or password is incorrect")
  else:
    break

# most data types allowed in a dictionary
new_users = {
  'llama': 'banana',
  'John': 'Wayne',
  'Jim': 'Morisson',
  1: 'does',
  3.4: 'This is ok',
  'string': 'this is a string',
  'lists': ['red', 'green', 'blue'],
  'dictionaries': {
    'first_name': 'something'
  }
}

accounts.update(new_users)

print(accounts)



'''
What are the key and value pair called together?
'''