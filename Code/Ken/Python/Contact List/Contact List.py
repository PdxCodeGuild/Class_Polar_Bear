import json

class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):
        import json
        # 1) open 'contacts.json' with option 'r' for read
        with open('Contacts.json', 'r') as j:
            # 2) get the text from the file
            entries  = j.read()
        # 3) convert the text into a python dictionary (json.loads)
            temp_dict = json.loads(entries)
        # 4) get the list of contacts out of the dictionary
            for contact in temp_dict['contacts']:
                if contact not in self.contacts:
                    self.contacts.append(contact)
        # 5) assign the list of dictionaries to self.contacts
        ...
    
    def count(self):
        # return the length of self.contacts
        return len(self.contacts)
    
    def save(self):
        # 1) open 'contacts.json' with open 'w' for write
        with open('Contacts.josn', 'w') as k:
        # 2) put self.contacts in a dictionary with the key 'contacts'
            contacts = {'contacts': self.contacts}
        # 3) convert the dictionary to a json string (json.dumps)
            contacts = json.dumps(contacts)
        # 4) write the json string to the file
            k.write(contacts)

    def print(self):
        # loop over self.contacts
        for contact in self.contacts:
        # print the information for each contact on a separate line
            print(contact)

    def add(self, name, phone_number, email):
        # create a new dictionary using the 3 parameters
        new_contact = {
            'name': name,
            'phone_number': phone_number,
            'email': email
        }
        # add the new dictionary to self.contacts
        self.contacts.append(new_contact)
    
    def remove(self, name):
        # find the contact in self-contacts with the given name
        for contact in self.contacts:
            if contact['name'].lower == name.lower():
         # remove the element at that index       
                self.contacts.pop(contact)
    
        
    def update(self, old_name, new_name, new_phone_number, new_email):
        # find the contact in self.contacts with the given old_name
        for contact in self.contacts:
        # set that contacts' name, phone number, etc to the given values
            if contact['name'].lower == old_name.lower:
                contact['name'] = new_name.title
                contact['phone_number'] = new_phone_number
                contact['email'] = new_email
            print(contact)
    
    
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
        print(f'Saved ${contact_list.count()} contacts.')
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
