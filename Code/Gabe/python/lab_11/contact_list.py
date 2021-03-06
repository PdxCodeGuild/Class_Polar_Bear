import json
c = open('lab_11/contacts.json')
contacts = json.loads(c.read())['contacts']
c.close()

class ContactList:
    def __init__(self):
        self.contacts = []

    def load(self):
        c = open('lab_11/contacts.json')
        self.contacts = json.loads(c.read())['contacts']
        c.close()
        return self.contacts
        ...

    def count(self):
        return len(self.contacts)
        ...

    def save(self):
        # 1) open 'contacts.json' with open 'w' for write
        # 2) put self.contacts in a dictionary with the key 'contacts'
        # 3) convert the dictionary to a json string (json.dumps)
        # 4) write the json string to the file
        with open('lab_11/contacts.json', 'w') as file:
          contacts = {'contacts': self.contacts}
          json_contacts = json.dumps(contacts)
          file.write(json_contacts)
        ...

    def print(self):
        # loop over self.contacts
        # print the information for each contact on a separate line
        for contact in self.contacts:
          print(
          f'''
            {contact['name']}
            {contact['phone_number']}
            {contact['email']}
          '''
          )
        ...

    def add(self, name, phone_number, email):
        # create a new dictionary using the 3 parameters
        # add the new dictionary to self.contacts
        new_dict = {'name': name, 'phone_number': phone_number, 'email': email}
        self.contacts.append(new_dict)
        ...

    def remove(self, name):
        # find the contact in self-contacts with the given name
        # remove the element at that index
        idx = None
        for i in range(len(self.contacts)):
          if self.contacts[i]['name'] == name:
            idx = i
        if idx:
          self.contacts.pop(idx)
        ...

    def update(self, old_name, new_name, new_phone_number, new_email):
        # find the contact in self.contacts with the given old_name
        # set that contacts' name, phone number, etc to the given values
        idx = None
        for i in range(len(self.contacts)):
          if self.contacts[i]['name'] == old_name:
            idx = i
        if idx:
          self.contacts[idx]['name'] = new_name
          self.contacts[idx]['phone_number'] = new_phone_number
          self.contacts[idx]['email'] = new_email
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