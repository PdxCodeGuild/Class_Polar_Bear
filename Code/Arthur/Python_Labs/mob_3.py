'''
Mob 3 - 1 October - It was a Friday - Credit Card Validation

Reece Adams
Ryan Gaston
Arthur Andama
James Thornton
'''


'''
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. 
The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:

4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
Valid!'''

'''
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. 
The steps are as follows:

Convert the input string into a list of ints
'''
user_input = list(input("Input a credit card #: "))
print(user_input)
# Slice off the last digit. That is the check digit.

check_digit = user_input[-1]

user_input.pop()
print(user_input)

# Reverse the digits.

user_input.reverse()
print(user_input, 'reverse')

# Double every other element in the reversed list.
# Example: [1,2,3,4] > [1,4,3,8]

change_user_input = []

for x in range(len(user_input)):
    user_input[x] = int(user_input[x])
    if x % 2 == 0:
        # print(x)
        user_input[x] = user_input[x] * 2
    print(x)
    change_user_input.append(user_input[x]) 
    print(change_user_input, "test")
print(change_user_input)

# Subtract nine from numbers over nine.

user_input_5 = []
for x in change_user_input:
    if x > 9:
        x = x - 9
        print(x, "testing x")
    user_input_5.append(x)
print(change_user_input)
print(user_input_5, "user input 5")    
        
# Sum all values.

sum_list = sum(user_input_5)
print(sum_list)

# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.

second_number = sum_list % 10
print(second_number)
print(check_digit, "check digit")
if int(second_number) == int(check_digit):
    print("your card number is valid")
else:
    print("your card is not valid")