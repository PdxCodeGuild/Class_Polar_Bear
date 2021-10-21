class ATM:

    def __init__(self):
        # initialize our class with a balance of 0 and an interest rate of 0.1
        self.current_balance = 0
        self.interest_rate = 0.1
        self.transactions = []
        ...

    def balance(self):
        # return the account balance
        return self.current_balance
        ...

    def deposit(self, amount):
        # add the given amount to the balance
        self.current_balance += amount
        self.transactions.append(f'User deposited ${amount}')
        ...

    def check_withdrawal(self, amount):
        # returns true if the withdrawn amount won't put the account in the negative, false otherwise
        if self.current_balance - amount >= 0:
          return True
        else:
          return False
        ...

    def withdraw(self, amount):
        # removes the given amount from the balance and returns it
        self.current_balance -= amount
        self.transactions.append(f'User withdrew ${amount}')
        return amount
        ...

    def deposit_interest(self):
        # calculate the amount of interest accumulated and add it to our balance
        # return the amount of interest added
        interest_amount = self.current_balance * self.interest_rate
        self.current_balance += interest_amount
        return interest_amount
        ...

    def print_transactions(self):
        return self.transactions

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
    elif command == 'transactions':
        trans_list = atm.print_transactions()
        for trans in trans_list:
            print(trans)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - get a list of transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
