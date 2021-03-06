# Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. The REPL below calls the methods of the class to simulate an ATM.

import math
class ATM:
    
    def __init__(self, acct_balance=0, interest =.001):
        # initialize our class with a balance of 0 and an interest rate of 0.1
        # 
        self.acct_balance = acct_balance
        self.interest = interest
        self.transaction = []
        # self.__account_balance = account_balance
        # self.__deposit = deposit

        ...
    
    def balance(self):
        # return the account balance
        # self.__account_balance = self.balance + (self.balance * self.interest)
        # return {self.__account_balance}
        return round(self.acct_balance, 2)
        ...
    
    def deposit(self, amount):
        # add the given amount to the balance
        self.acct_balance += amount
        
        return self.acct_balance
        ...
    
    def check_withdrawal(self, amount):
        if amount <= self.acct_balance:
            return True
        else:
            return False
        
        # returns true if the withdrawn amount won't put the account in the negative, false otherwise
        ...
    
    def withdraw(self, amount):
        # removes the given amount from the balance and returns it
        self.acct_balance -= amount
        return self.acct_balance
        ...
    
    def deposit_interest(self):
        # calculate the amount of interest accumulated and add it to our balance
        # return the amount of interest added
        deposit_interest = self.acct_balance * self.interest
        # add_interest = self.acct_balance
        # print(type(add_interest))
        # print(type(deposit_interest))
        # self.balance = add_interest + deposit_interest

        return deposit_interest
        ...
    def print_transactions(self, amount, transaction_type):
        transaction = f'User {transaction_type} ${amount}'
        self.transaction_list.append(transaction)
        

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
