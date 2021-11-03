# Reece Adams - lab17.py - lab 17 - Contact List #

import json

class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):
        with open('contacts.json', 'r') as file:
            file = json.loads(file.read())
        for key in file['contacts']:
            self.contacts.append(key)
    
    def count(self):
            return len(self.contacts)
    
    def save(self):
        with open('contacts.json', 'w') as file:
            file.write(json.dumps({'contacts':self.contacts},indent=2))
            
    def print(self):
        print(f'\n')
        for key in self.contacts:
            name=key['name']
            phone_number=key['phone_number']
            email=key['email']
            print(f'{name}, Phone number: {phone_number}, Email: {email}\n')

    def add(self, name, phone_number, email):
        new_dict = {'name': name, 'phone_number': phone_number, 'email': email}
        self.contacts.append(new_dict)
    
    def remove(self, name):
        for key in self.contacts:
            if name == key['name']:
                self.contacts.remove(key)
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        for key in self.contacts:
            if old_name == key['name']:
                self.contacts.remove(key)
                new_dict = {'name': new_name, 'phone_number': new_phone_number, 'email': new_email}
                self.contacts.append(new_dict)

contact_list = ContactList()
contact_list.load()
print('Welcome to the Contact List App (CLA)')
while True:
    command = input('Enter a command: ')
    if command == 'load':
        contact_list.load()
        print(f'Loaded {contact_list.count()} contacts.')
    elif command == 'count':
        print(contact_list.count())
    elif command == 'save':
        contact_list.save()
        print(f'Saved {contact_list.count()} contacts.')
    elif command == 'print':
        contact_list.print()
    elif command == 'add':
        print('Enter info of contact to add:')
        name = input('Name: ').title()
        phone_number = input('Phone Number: ')
        email = input('Email: ')
        contact_list.add(name, phone_number, email)
    elif command == 'remove':
        name = input('Name of contact to remove: ').title()
        contact_list.remove(name)
    elif command == 'update':
        print('Enter info of contact to add:')
        old_name = input('Name of contact to update: ').title()
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