'''
Blackjack Advice Version 1
'''

import string

# create dictionary with cards and their values
cards_value = {
    'A' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10,
}

# display the cards and ask user to pick 3
cards = "A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K"
print(cards)

user_points = 0


# function to verify user input matches the given options
def verify(user_input):
    if user_input not in cards_value:
        return False
    else:
        return True

# Function to verify correct user input and add the value of the cards chosen by the user
def short(user_card_number, card_number):
    user_points = 0
    while True:
        user_card_number = str.upper(user_card_number)
        check = verify(user_card_number)
        if check == False:
            print("Invalid entry. Please try again.")
            user_card_number = input(f"Please select your \033[1m{card_number}\033[0;0m card from the options above: ")

            continue

        user_points += cards_value.get(user_card_number)
        break
    return user_points


# while True:
#     while True:
#         user_card_one = input("1- Please select your \033[1mFIRST\033[0;0m card from the options above: ")
#         user_card_one = str.upper(user_card_one)
#         check = verify(user_card_one)
#         if check == False:
#             print("Invalid entry. Please try again.")
#             continue
#         user_points =+ cards_value.get(user_card_one)
#         break

#     while True:
#         user_card_two = input("2- Please select your \033[1mSECOND\033[0;0m card from the options above: ")
#         user_card_two = str.upper(user_card_two)
#         check = verify(user_card_two)
#         if check == False:
#             print("Invalid entry. Please try again.")
#             continue
#         user_points += cards_value.get(user_card_two)
#         break

#     while True:
#         user_card_three = input("3- Please select your \033[1mTHIRD\033[0;0m card from the options above: ")
#         user_card_three = str.upper(user_card_three)
#         check = verify(user_card_three)
#         if check == False:
#             print("Invalid entry. Please try again.")
#             continue
#         user_points += cards_value.get(user_card_three)

#         break
    
#     break


# shorter version using a function to avoid repeating code
while True:
    user_card_one = input("Please select your \033[1mFIRST\033[0;0m card from the options above: ")
    user_points += short(user_card_one, 'FIRST')

    user_card_two = input("Please select your \033[1mSECOND\033[0;0m card from the options above: ")
    user_points += short(user_card_two, 'SECOND')

    user_card_three = input("Please select your \033[1mTHIRD\033[0;0m card from the options above: ")
    user_points += short(user_card_three, 'THIRD')
    
    break

if user_points < 17:
    print(f"You have {user_points} points, hit!")
elif user_points >= 17:
    print(f"You have {user_points} points, stay!")
elif user_points == 21:
    print(f"You have {user_points} points, BlackJack!")
else:
    print(f"You have {user_points} points, already busted!")

    