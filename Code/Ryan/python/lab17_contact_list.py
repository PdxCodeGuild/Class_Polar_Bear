import json
class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):
        # 1) open 'contacts.json' with option 'r' for read
        with open('contacts.json', 'r') as data:
        # 2) get the text from the file
            text = data.read()
        # 3) convert the text into a python dictionary (json.loads)
            contacts_dict = json.loads(text)
        # 4) get the list of contacts out of the dictionary
            # print(contacts_dict['contacts'])
        #     list_of_contacts = []
        #     for contact in range(len(contacts_dict['contacts'])):
        #         list_of_contacts.append(contacts_dict['contacts'][contact])
        # # 5) assign the list of dictionaries to self.contacts
        self.contacts = contacts_dict['contacts']
        ...
    
    def count(self):
        # return the length of self.contacts
        return f'{len(self.contacts)}'
        ...
    
    def save(self):
        # 1) open 'contacts.json' with open 'w' for write
        with open('contacts.json', 'w') as data:
        # 2) put self.contacts in a dictionary with the key 'contacts'
            saved_contacts = {'contacts': self.contacts}
        # 3) convert the dictionary to a json string (json.dumps)
            json_contacts = json.dumps(saved_contacts)
        # 4) write the json string to the file
            data.write(json_contacts)
        ...

    def print(self):
        # loop over self.contacts
        # for contact in range(len(self.contacts)):
        #     print(f"""
        #     {self.contacts[contact]['name']}
        #     {self.contacts[contact]['phone_number']}
        #     {self.contacts[contact]['email']}""")
# both work but below is cleaner (above would be needed if adjustments to the list needed to occur)
        for contact in self.contacts:
            print(f"""
            {contact['name']}
            {contact['phone_number']}
            {contact['email']}
            {'-'*50}""")
        # print the information for each contact on a separate line

        ...

    def add(self, name, phone_number, email):
        # create a new dictionary using the 3 parameters
        new_dictionary = {'name': name, 'phone_number': phone_number, 'email': email}
        # add the new dictionary to self.contacts
        self.contacts.append(new_dictionary)
        ...
    
    def remove(self, name):
        # find the contact in self-contacts with the given name
        for contact in range(len(self.contacts)):
            if name.lower() in self.contacts[contact]['name'].lower():
                self.contacts.remove(contact)
        # remove the element at that index

        ...
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        # find the contact in self.contacts with the given old_name
        # set that contacts' name, phone number, etc to the given values
        self.add(new_name, new_phone_number, new_email)
        self.remove(old_name)
        
        # for contact in range(len(self.contacts))
        # for contact in self.contacts:
        #     if contact['name']==old_name
        #     # if old_name == self.contacts[contact]['name'].lower():
        #         contact.update({
        #             'name': new_name,
        #             'email': new_email,
        #             'phone_number': new_phone_number
        #         })
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
