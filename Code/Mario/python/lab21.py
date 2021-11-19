class ATM:

    def __init__(self):
        self.account_balance = 0
        self.interest_rate = 0.1

    def balance(self):
        return self.account_balance

    def deposit(self, amount):
        # pass
        self.account_balance += amount
        self.print_transaction('deposited', amount)

    def check_withdrawal(self, amount):
        if self.account_balance - amount > 0:
            self.print_transaction('withdrew', amount)
            return True
        else:
            return False

    def withdraw(self, amount):
        self.account_balance -= amount
        return self.account_balance

    def deposit_interest(self):
        return self.account_balance * self.interest_rate

    def print_transaction(self, transaction_type, amount):
        print(f"User {transaction_type}: {amount}")


atm = ATM()  # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance()  # call the balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount)  # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.deposit_interest()  # call the calc_interest() method
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
