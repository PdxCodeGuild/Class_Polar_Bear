# \' deals with single quote strongs
# \n starts wrapping at this point 
# \t acts as a tab spacing
# r'' raw string, prints string exactly what is in quotes / Useful for File Path or regex

# multi line 

# message = '''This
# is
# a
# multi
# line
# string'''

# print(message)

# can multiply a string to print more than once
# print('=' * 50)
# text = 'sometext'
# fourth_char = text[3]
# last_char = text[-1]

# subset = text[0:4] # 2nd number is non-inclusive 1st number is inclusive
# subset1 = text[0:] # grabs whole string, goes to end
# subset3 = text[1:2:3] # increments
# reverseString = text[::-1]
# print(fourth_char + last_char + subset + subset1 + reverseString)



# hello = 'Hello World'
# test = hello.find(7)
# hellovtwo = hello[test:]
# find('o', 5) 

# ss = hello[6:]

# print(ss)

# .title() Capitalizes every word

string = 'Hello World'

print(string.startswith('Hello')) # true
print(string.endswith('d')) # true
print('Worl' in string) # True
print('x' in string) # false