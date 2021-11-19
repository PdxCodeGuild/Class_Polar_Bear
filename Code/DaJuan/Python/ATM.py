# ATM

#Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. The REPL below calls the methods of the class to simulate an ATM.

## Part 1

#python
transactions_list = []
class ATM:
    
    
    def __init__(self, balance = 0, interest_rate = 0.1):
        self.account_balance = balance
        self.interest_rate = interest_rate
        # initialize our class with a balance of 0 and an interest rate of 0.1
        ...
    
    def balance(self):
        return self.balance
        # return the account balance
        ...
    
    def deposit(self, amount):
        self.account_balance += amount
        
        # add the given amount to the balance
        ...
    
    def check_withdrawal(self, amount):
        if self.account_balance -= amount < 0:
            return False
        return True
        # returns true if the withdrawn amount won't put the account in the negative, false otherwise
        ...
    
    def withdraw(self, amount):
        self.account_balance -= amount
        return self.account_balance
        
        # removes the given amount from the balance and returns it
        ...
    
    def deposit_interest(self):
        # calculate the amount of interest accumulated and add it to our balance
        balance_x_interest = self.balance * self.interest_rate
        balance_post_interest = self.balance + balance_x_interest
        # return the amount of interest added
        return balance_post_interest

    def print_transactions(self, amount, transaction_type):
        transaction = f'user {transaction_type} ${amount}'
        return transactions_list
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
        deposit_stmt = f'user deposited {amount}'
        transactions_list.append(deposit_stmt)
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
            withdrawal_stmt = f'user withdrew {amount}'
            transactions_list.append(withdrawal_stmt)
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.deposit_interest() # call the calc_interest() method
        
        print(f'Deposited ${amount} in interest')
    elif command == 'transactions':
        atm.print_transactions()
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


## Part 2

#'''Have the ATM maintain a list of transactions. Every time the user makes a deposit 
#or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. 
#Add a new method `print_transactions()` to your class for printing out the list of transactions.
#''




