import datetime
class ATM:
    
    def __init__(self):
        # initialize our class with a balance of 0 and an interest rate of 0.1
        self.current_balance=0
        self.interest_rate=0.1
        self.transactions =[]
        ...
    
    def balance(self):
        # return the account balance
        time=datetime.datetime.now()
        self.transactions.append(f'{time}: user checked balance ({self.current_balance}).')
        return self.current_balance
        ...
    
    def deposit(self, amount):
        # add the given amount to the balance
        time=datetime.datetime.now()
        self.current_balance+=amount
        self.transactions.append(f'{time}: user deposited {amount}.')
        ...
    
    def check_withdrawal(self, amount):
        # returns true if the withdrawn amount won't put the account in the negative, false otherwise
        if amount <= self.current_balance:
            return True
        else:
            return False
        ...
    
    def withdraw(self, amount):
        # removes the given amount from the balance and returns it
        time=datetime.datetime.now()
        self.current_balance-=amount
        self.transactions.append(f'{time}: user withdrew {amount}.')
        return self.current_balance
        ...
    
    def deposit_interest(self):
        # calculate the amount of interest accumulated and add it to our balance
        time=datetime.datetime.now()
        interest=self.current_balance*self.interest_rate
        self.current_balance+=interest
        self.transactions.append(f'{time}: interest of {interest} accrued.')
        # return the amount of interest added
        return interest
        ...

    def print_transactions(self):
        print('Transactions:\n')
        for i in self.transactions:
            print(f'{i}')
        ...


atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.deposit_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Deposited ${amount} in interest')
    elif command == 'print':
        atm.print_transactions()
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('print    - print transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break

    else:
        print('Command not recognized')
