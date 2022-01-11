# -------------- #
# Python Lab 21
# ATM
#--------------- #

class ATM:
    
    def __init__(self):
        self._balance = 0
        self._interest_rate = 0.1
        self._transaction_history = []
    
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def check_withdrawal(self, amount):
        return self._balance - amount >= 0

    def withdraw(self, amount):
        self._balance -= amount
        return self._balance
    
    def deposit_interest(self):
        return (self._balance * self._interest_rate) / 100

    def print_transactions(self):
        for i, t in enumerate(self._transaction_history, 1):
            print(f"{i}. {t}")

    def add_transaction(self, text):
        self._transaction_history.append(text)

atm = ATM()
print('Welcome to the ATM! / Bienvenue au guichet automatique !')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance()
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount)
        print(f'Deposited ${amount}')
        atm.add_transaction(f"User deposited {amount}$")
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)
            print(f'Withdrew ${amount}')
            atm.add_transaction(f"User witdrew {amount}$")
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.deposit_interest()
        atm.deposit(amount)
        print(f'Deposited ${amount} in interest')
    elif command == 'transactions':
        print("Transactions history: ")
        atm.print_transactions()
    elif command == 'help':
        print('Available commands:')
        print('balance: obtain the current balance')
        print('deposit: deposit money')
        print('withdraw: withdraw money')
        print('interest: accumulate interest')
        print('transactions: print transactions history')
        print('exit: exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')

#--------------- #