# for dict in withdraw_deposit:
#             for key in dict:
#                 if 'deposit' in key:
#                     dep = dict['deposit']
#                     print(f"\tYou deposited: ${dep}")
#                 elif 'withdraw' in key:
#                     wit = dict['withdraw']
#                     print(f"\tYou withdrew: ${wit}")
#                 elif 'interest_dep' in key:
#                     int_dep = dict['interest_dep']
#                     print(f"\tInterest gained: ${int_dep}")
#             bal = atm.balance()

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
    return message
