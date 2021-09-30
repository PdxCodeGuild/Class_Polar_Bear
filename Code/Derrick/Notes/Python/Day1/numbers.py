import math
import random
import some_module

4       # int
2.3     # float

# a = 2.2
# b = 4.4

# print(a + b)
# print(a - b)
# print(a * b)
# print(a ** b) # exponent
# print(a / b) # division always returns a float
# print(b // a) # this will return an integer instead of float 'floor division', unless one of the numbers is already a float
# print(b % a) # good way to determine even/odd: if b % 2 == 0 "even"

# shorthands
# a += b
# -=
# *=
# /=
# //=
# %=

c = 3.6

# rounds up or down, nearest whole number
print(round(c)) 

# # round to specified decimal

# round(c,3) # second value is how many decimals you want to round to
# abs() # returns positive value
# min() # returns smallest number
# max() # returns highest number
# sum(x,y)

# Math module functionality

print(math.floor(598.123)) # Rounds down to whole number

print(math.ceil(598.123)) # Rounds up to whole number

print(math.pi)

pi = str(math.pi);

print(len(pi) - 2)

# Random module functionality

print(random.randint(0,5000000)) # gives random number between 2 numbers

# random.choice() # random digit from object or list

print(random.choice(pi))

print(some_module.secretKey)

# try:
#     raise ValueError Forces exception declared below