from typing import Text
import json

class ContactList():
    
    def __init__(self):
        self.contacts = []

    def load(self):
        # 1) open 'contacts.json' with option 'r' for read
        with open('contacts.json', 'r') as file:
            data = json.load(file)

        # 2) get the text from the file
        # 3) convert the text into a python dictionary (json.loads)


        # 4) get the list of contacts out of the dictionary
        file_list = data["contacts"]

        # 5) assign the list of dictionaries to self.contacts
        self.contacts = file_list
        ...
    
    def count(self):
        # return the length of self.contacts
        return len(self.contacts)
        ...
    
    def save(self):
        # 1) open 'contacts.json' with open 'w' for write
        with open('contacts.json', 'w') as file_w: 
                   
            # 2) put self.contacts in a dictionary with the key 'contacts'
            contacts_dictionary = {
                'contacts':self.contacts
            }
                
            # 3) convert the dictionary to a json string (json.dumps)
            contacts_dictionary = json.dumps(contacts_dictionary)

            # 4) write the json string to the file
            file_w.write(contacts_dictionary)
        ...

    def print(self):
        # loop over self.contacts
        for i in range(len(self.contacts)):
            # print the information for each contact on a separate line
            print(self.contacts[i]['name'])
            print(self.contacts[i]['phone_number'])
            print(self.contacts[i]['email'])
            print('\n')
        ...

    def add(self, name, phone_number, email):
        # create a new dictionary using the 3 parameters
        # add the new dictionary to self.contacts
        new_dictionary = {
            'name':name,
            'phone_number':phone_number,
            'email':email
        }

        self.contacts.append(new_dictionary)
        ...
    
    def remove(self, name):
        # find the contact in self-contacts with the given name
        for i in range(len(self.contacts)):
            if self.contacts[i] == name:
                # remove the element at that index
                self.contacts.remove(self.contacts[i]) 
        ...
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        # find the contact in self.contacts with the given old_name       
        for i in range(len(self.contacts)):
            if old_name in self.contacts[i]['name']:
                # set that contacts' name, phone number, etc to the given values
                self.contacts[i] = {
                    "name": new_name,
                    "phone_number": new_phone_number,
                    "email": new_email
                }

        
        ...
    
contact_list = ContactList() # create an instance of our class
contact_list.load()
print('Welcome to the Contact List App (CLA)')
while True:
    command = input('Enter a command: ')
    if command == 'load':
        contact_list.load()
        print(f'Loaded ${contact_list.count()} contacts.')
    elif command == 'save':
        contact_list.save()
        print(f'Saved {contact_list.count()} contacts.')
    elif command == 'print':
        contact_list.print()
    elif command == 'add':
        print('Enter info of contact to add:')
        name = input('Name: ')
        phone_number = input('Phone Number: ')
        email = input('Email: ')
        contact_list.add(name, phone_number, email)
    elif command == 'remove':
        name = input('Name of contact to remove: ')
        contact_list.remove(name)
    elif command == 'update':
        print('Enter info of contact to add:')
        old_name = input('Name of contact to update: ')
        new_name = input('New Name: ')
        new_phone_number = input('New Phone Number: ')
        new_email = input('New Email: ')
        contact_list.update(old_name, new_name, new_phone_number, new_email)
    elif command == 'help':
        print('Available commands:')
        print('load   - load all contacts from the file')
        print('save   - save contacts to a file')
        print('print  - print all contacts')
        print('add    - add a new contact')
        print('remove - remove a contact')
        print('update - update a contact')
        print('exit   - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
