
class ATM:
    
    def __init__(self):
        # initialize our class with a balance of 0 and an interest rate of 0.1
        self.account_balance = 0
        self.interest = 0.001
        self.transaction_list = []
    
    def balance(self):
        # return the account balance
        return round(self.account_balance, 2)
    
    def deposit(self, amount):
        # add the given amount to the balance
        self.account_balance += amount
    
    def check_withdrawal(self, amount):
        # returns true if the withdrawn amount won't put the account in the negative, false otherwise
        if self.account_balance - amount < 0:
            return False
        return True
    
    def withdraw(self, amount):
        # removes the given amount from the balance and returns it
        self.account_balance -= amount
        return self.account_balance
    
    def deposit_interest(self):
        # calculate the amount of interest accumulated and add it to our balance
        # return the amount of interest added
        interest = self.interest * self.account_balance
        self.account_balance += interest
        self.print_transactions(interest, 'interest deposit')
        return interest

    def print_transactions(self, amount, transaction_type):
        transaction = f'User {transaction_type} ${amount}'
        self.transaction_list.append(transaction)
        return self.transaction_list



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
        atm.print_transactions(amount, 'Deposited')
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            atm.print_transactions(amount, 'Withdrew')
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.deposit_interest() # call the calc_interest() method
        print(f'Deposited ${amount} in interest')
    elif command == 'statement':
        for i in range(len(atm.transaction_list)):
            print(atm.transaction_list[i])
        print(f'Current balance is ${atm.balance()}')
    elif command == 'help':
        print('Available commands:')
        print('balance   - get the current balance')
        print('deposit   - deposit money')
        print('withdraw  - withdraw money')
        print('interest  - accumulate interest')
        print('statement - view transactions')
        print('exit      - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
