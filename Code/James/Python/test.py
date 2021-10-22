'''
with open('contacts.json', 'r') as file:
# 2) get the text from the file
    import requests
    text = file.json()
    response = requests.get(file)
# 3) convert the text into a python dictionary (json.loads)
    text2 = response.json
    print(text)
    print(text2)
'''
'''
f = open('contacts.json')  # open the file
contents = f.read()  # read the contents
# contents2 = contents.json()
print(contents)
'''
# print(data['contacts'][1]['name']) # prints a name

'''
list=[]
import json
with open('contacts.json', 'r') as file:
    data = json.load(file)
    # print(data)

for contact in data['contacts']:
    list.append(contact)
# print(list)

dictionary2 = {'contacts':[]}
dictionary2['contacts'] += list

with open('contacts_copy.json', 'w') as file2:
    data2 = json.dumps(dictionary2)
    file2.write(data2)
'''



contacts = [{
        "name": "Dora M. Smith",
        "phone_number": "919-781-7129",
        "email": "doramsmith@hotmail.com"
    },{
        "name": "Annette D. Berube",
        "phone_number": "662-319-6954",
        "email": "annette@gmail.com"
    },{
        "name": "Austin M. Pigott",
        "phone_number": "478-777-8878",
        "email": "austin@aol.com"
    }]

zero = contacts[0]
one = contacts[1]
two = contacts[2]
for value in zero:
    print(zero[value])
# print(contacts[0]['name'])
