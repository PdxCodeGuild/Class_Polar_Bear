# user login with dictionary to store username and password
accounts = {
    'username' : 'password',
    'Batman' : 'notbrucewayne1'
}

while True:
    choice = input('Select (1) Sign up, or (2) Login, or (3) Quit: ')
    if choice == '1':

# sign up new user(can not be taken)
        username= input('Enter a username: ')
        password = input('Enter a password: ')

        if username in accounts:
            print('username already exists')
            continue
        else:
            accounts[username] = password

    elif choice == '2':
# Login user
        username= input('Enter a username: ')
        password = input('Enter a password: ')

        if accounts.get(username) == password:
            print(f'welcome{username}')
        else:
            print('username or password incorrect')
    else:
        break
        


