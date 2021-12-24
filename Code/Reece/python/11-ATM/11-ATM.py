# Reece Adams - Lab 11 in class - lab 21 - ATM #

# Part 1 #

# class ATM:
    
#     def __init__(self):
#         self.bal = {
#             'balance':0,
#             'interest_rate': 0.1
#         }
    
#     def balance(self):
#         return self.bal['balance']
    
#     def deposit(self, amount):
#         self.bal['balance'] += amount
    
#     def check_withdrawal(self, amount):
#         if self.bal['balance'] - amount > -1:
#             return True
#         else:
#             return False
    
#     def withdraw(self, amount):
#         self.bal['balance'] -= amount
    
#     def deposit_interest(self):
#         # calculate the amount of interest accumulated and add it to our balance
#         amount = self.bal['balance'] * 0.1
#         # return the amount of interest added
#         return amount

# atm = ATM() # create an instance of our class
# print('Welcome to the ATM')
# while True:
#     command = input('Enter a command: ')
#     if command == 'balance':
#         balance = atm.balance() # call the balance() method
#         print(f'Your balance is ${balance}')
#     elif command == 'deposit':
#         amount = float(input('How much would you like to deposit? '))
#         atm.deposit(amount) # call the deposit(amount) method
#         print(f'Deposited ${amount}')
#     elif command == 'withdraw':
#         amount = float(input('How much would you like '))
#         if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
#             atm.withdraw(amount) # call the withdraw(amount) method
#             print(f'Withdrew ${amount}')
#         else:
#             print('Insufficient funds')
#     elif command == 'interest':
#         amount = atm.deposit_interest() # call the calc_interest() method
#         atm.deposit(amount)
#         print(f'Deposited ${amount} in interest')
#     elif command == 'help':
#         print('Available commands:')
#         print('balance  - get the current balance')
#         print('deposit  - deposit money')
#         print('withdraw - withdraw money')
#         print('interest - accumulate interest')
#         print('exit     - exit the program')
#     elif command == 'exit':
#         break
#     else:
#         print('Command not recognized')

# Part 2 #

class ATM:
    
    def __init__(self):
        self.bal = {
            'balance':0,
            'interest_rate': 0.001
        }
    
    def balance(self):
        return self.bal['balance']
    
    def deposit(self, amount):
        self.bal['balance'] += amount
    
    def check_withdrawal(self, amount):
        if self.bal['balance'] - amount > -1:
            return True
        else:
            return False
    
    def withdraw(self, amount):
        self.bal['balance'] -= amount
    
    def deposit_interest(self):
        # calculate the amount of interest accumulated and add it to our balance
        amount = self.bal['balance'] * self.bal['interest_rate']
        # return the amount of interest added
        return amount

withdraw_deposit = []

def total_transactions(info):
    for dict in info:
            for key in dict:
                if 'deposit' in key:
                    dep = dict['deposit']
                    message = f"\tYou deposited: ${dep}"
                elif 'withdraw' in key:
                    wit = dict['withdraw']
                    message = f"\tYou withdrew: ${wit}"
                elif 'interest_dep' in key:
                    int_dep = dict['interest_dep']
                    message = f"\tInterest gained: ${int_dep}"
                bal = atm.balance()
    return bal

atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        print(f'\nYour balance is ${balance}\n')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'\nDeposited ${amount}\n')
        if amount != '':
            withdraw_deposit.append({'deposit':amount})
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'\nWithdrew ${amount}\n')
        if amount != '':
            withdraw_deposit.append({'withdraw':amount})
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.deposit_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Deposited ${amount} in interest')
        if amount != '':
            withdraw_deposit.append({'interest_dep':amount})
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        print('\nHere is a list of your transactions:\n')
        total_transactions(withdraw_deposit)
        print(f'\n----------------------------------------------------------')
        print(f"\nYour final balance is: ${total_transactions(withdraw_deposit)}\n")
        break
    else:
        print('Command not recognized')