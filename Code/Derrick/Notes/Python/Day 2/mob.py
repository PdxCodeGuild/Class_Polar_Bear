import random 

# x = random.randint(1,10)
# counter = 0
# max_num = 10
# current_num = 0 

# while True:
#     userInput = input('guess number')
#     try:
#         userInput = int(userInput)
#     except ValueError:
#         continue
#     if userInput < 0 or userInput > max_num:
#         print('Invalid Number')
#         counter += 1
#         continue
#     if counter == 10:
#         print('You ran out of tries.')
#         break
#     if userInput != x:
#         current_num = userInput
#         if counter == 0:
#             if userInput < x:
#                 print('Too low.  Try again')
#             else:
#                 print('Too high.  Try again')
        
#         else:
#             if abs(userInput - x) < abs(current_num - x):
#                 print('closer')
#             else:
#                 print('Getting further') 
#         counter += 1 
        
#     else:
#         print('Congrats.  You win') 
#         break      
# 
userNum = int(input('Choose a number for the computer to guess'))

while True:
    computer = random.randint(1,5)
    if userNum == computer:
        print(f'Your number was {userNum}')
        break
    else: 
        print(f'guessing....{computer}')
        continue
