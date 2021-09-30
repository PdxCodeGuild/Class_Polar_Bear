# greeting = 'Good Evening '
# # f
# number = int(input('Enter a number: '))
# # print(greeting + helloTo)
# # print(f'Hello {helloTo}!')

# print(type(number))
# print(2 + number)

# String 
# Int 
# Float 
# boolean 
# None 

userInput = input('enter a number')

# perform action
try: 
    userNumber = int(userInput)
    
# if error happens run this code and don't run the rest
except ValueError: 
    print('No number provided')
    exit()

if userNumber > 0:
    print('positive number')
elif userNumber == 0:
    print('zero')
else:
    print('negative number')