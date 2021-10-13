# SEE UPDATED CODE IN JAMES MOB FOLDER

# 03 Credit Card Validation.md
# Credit Card Validation
# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:
# 1. Convert the input string into a list of ints
original_user_input = list(input('Input your card number: ')) #[1, 2, 3, 10, 5]

user_input = []
for y in original_user_input:
    y = int(y)
    #print(f'{type(y)}')
    user_input.append(y)
#print(user_input)

print(f'1. {user_input}')
check_digit = user_input[-1]
# 2. Slice off the last digit. That is the check digit.
user_input.pop()
print(f'2. {user_input}')


# 3. Reverse the digits.
user_input.reverse()
print(f'3. {user_input}')
# 4. Double every other element in the reversed list.
changed_user_input = []
for x in user_input:
    if x % 2 == 0:
        x = x * 2
    print(x)
    changed_user_input.append(x)
print(f'4. {changed_user_input}')

# 5. Subtract nine from numbers over nine.
user_input_5 = []
for x in changed_user_input:
    if x > 9:
        x = x - 9
    #print(x)
    user_input_5.append(x)
print(f'5. {user_input_5}')
# 6. Sum all values.
sum_list = sum(user_input_5)
print(f'6. {sum_list}')
# 7. Take the second digit of that sum.
second_number = sum_list % 10 
print(second_number)

# 8. If that matches the check digit, the whole card number is valid.
if second_number == check_digit:
    print('your card number is Valid')
else:
    print('your card is not valid')

# For example, the worked out steps would be:
# 1. 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 2. 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 3. 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 4. 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 5. 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 6. 85
# 7. 5
# 8. Valid!
