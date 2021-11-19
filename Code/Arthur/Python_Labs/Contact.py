import json
class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):
        # 1) open 'contacts.json' with option 'r' for read
        # 2) get the text from the file
        # 3) convert the text into a python dictionary (json.loads)
        # 4) get the list of contacts out of the dictionary
        # 5) assign the list of dictionaries to self.contacts
        ...

        with open('C:/Users/REACT/Desktop/pdx_code/New_Polar/Code/Arthur/Python_Labs/contacts.json') as file:
            output_data = json.loads(file.read())

            self.contacts=output_data['contacts']
    
    def count(self):
        # return the length of self.contacts
        ...
        return len(self.contacts)
    
    def save(self):
        # 1) open 'contacts.json' with open 'w' for write
        # 2) put self.contacts in a dictionary with the key 'contacts'
        # 3) convert the dictionary to a json string (json.dumps)
        # 4) write the json string to the file
        ...
        with open('C:/Users/REACT/Desktop/pdx_code/New_Polar/Code/Arthur/Python_Labs/contacts.json','w') as file :
            output_data = {'contacts':self.contacts}
            json_contacts =json.dumps(output_data)
            file.write(json_contacts)

    def print(self):
        # loop over self.contacts
        # print the information for each contact on a separate line
        ...
        #if we need to modify the list use i but if we don't need to modify then just use for contact in self.contacts
        # for i in range(len(self.contacts)):
        #     print(self.contacts)
       
        for contact in self.contacts:
            print(contact['name'])
            print(contact['email'])
            print(contact['phone_number'])
            print('---------\n')


    def add(self, name, phone_number, email):
        # create a new dictionary using the 3 parameters
        # add the new dictionary to self.contacts
        ...

        dictionary ={
            'name': name,
            'phone_number':phone_number,
            'email':email
        }
        self.contacts.append(dictionary)
    
    def remove(self, name):
        # find the contact in self-contacts with the given name
        # remove the element at that index
        ...
        for contact in self.contacts:
            # if name == contact['name']: this one is an exact match 
            if name in contact['name'].lower():
                self.contacts.remove(contact)
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        # find the contact in self.contacts with the given old_name
        # set that contacts' name, phone number, etc to the given values
        ...

        # if you are to modify anything use this
        # for i in range(len(self.contacts)):

        for contact in self.contacts:
            if contact['name'] == old_name:
                contact.update({
                        'name':new_name,
                        'email':new_email,
                        'phone_number' :new_phone_number
                    })
                    #contact['name] = new_name
                    #contact['email']= new_email
                    #contact['phone_number']= new_phone_number
        #another method
        # Self.add(new_name,new_phone_number,new_email)
        # self.remove(old_name)

    
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