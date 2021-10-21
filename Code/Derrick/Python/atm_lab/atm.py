class ATM:
    
    def __init__(self,atm_balance=0,rate=0.1):
        self.atm_balance = atm_balance
        self.rate = rate
        self.transactions = []
    
    def balance(self):
        return self.atm_balance
    
    def deposit(self, amount):
        self.atm_balance += amount
        self.transactions.append(f'+ User deposited ${amount}')
    
    def check_withdrawal(self, amount):
        total = self.atm_balance - amount

        if total < 0:
            return False

        return True 
    
    def withdraw(self, amount):
        self.atm_balance -= amount
        self.transactions.append(f'- User withdrew ${amount}')
        return amount
    
    def deposit_interest(self):
        amount = self.atm_balance * self.rate
        self.atm_balance += amount
        self.transactions.append(f'+ User deposited ${amount}')
        return amount
    
    def print_transactions(self):
        for transaction in self.transactions:
            if self.transactions.index(transaction) == len(self.transactions) - 1:
                print('-' * 50)
                print(transaction)
                print('-' * 50)
                break 

            print('-' * 50)
            print(transaction)


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
        # atm.deposit(amount) 
        print(f'Deposited ${amount} in interest')
    elif command == 'print':
        atm.print_transactions() # call the print_transactions() method
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('print    - show all transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
