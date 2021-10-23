class ATM:
    
    def __init__(self):
        # initialize our class with a balance of 0 and an interest rate of 0.1
        self.balance = 0
        self.interest = 0.001
        self.trans = []
    
    def balance(self):
        # return the account balance
        return self.balance

    def check_withdrawal(self, amount):
        # returns true if the withdrawn amount won't put the account in the negative, false otherwise
        if self.balance < amount:
            return False
        return True
    
    def deposit(self, amount):
        # add the given amount to the balance
        self.balance += amount
        self.trans.append(f'deposit of ${amount}')

    def deposit_interest(self):
        # calculate the amount of interest accumulated and add it to our balance
        # return the amount of interest added
        gain = self.balance*self.interest
        self.balance += gain
        return gain

    def print_transactions(self):
        for t in self.trans:
            print(t)

    def withdraw(self, amount):
        # removes the given amount from the balance and returns it
        self.balance -= amount
        self.trans.append(f'withdrawal of ${amount}')
        return self.balance()

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
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')

