# dictionary = {'first':'Derrick','last':'Johnson','pet':'Enzo'}

# dictionary['newKey'] = 'new value'

# dictionary['nickname'] = 'NICKNAME'
# # dictionary.get('second new key','No nickname dude')
# nickname = dictionary.get('nickname', False)

# # print(dictionary.get('second new key','No nickname dude'))

# # if nickname:
# #     print('has nickname')
# # else:
# #     print('no nickname')

# del dictionary['nickname']

# # print(dictionary)

# # if 'pet' in dictionary:
# #     print(f'This person\'s pet\'s name is {dictionary['pet']})

# colors = ['red','blue','green']

# for key in dictionary:
#     key = 'test'

# print(dictionary)

users = {
    'jim': 'halpert',
    'michael': 'scott'
}

while True:
    loginOrCreate = input('1 to sign up, 2 to login')
    if loginOrCreate == '1':
        # signup
        username = input('Enter user name')
        pw = input('Enter password')

        if username in users:
            print('Different user name')
            continue
        else:
            users[username] = pw
            break

    elif loginOrCreate == '2':
        username = input('Enter user name')
        pw = input('Enter password')
        if users.get(username) == pw:
            print(f'Welcome {username}')
        else:
            print('Incorrect')
        break
    else:
        break

print(users)