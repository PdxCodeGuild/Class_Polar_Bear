# ### Built-in funtion
# # Anytime you need to call a function you add open and close parenthesis after function name.
# print('Some message') # that lets you print into term
# input('Some prompt') # lets a user type in an input
# int('567')
# float()
# str()
# list()


# # Some functions can take multiple args
# sum(4, 5, 6)


# # Create out own
# def speak_message(note):
#   return print(note)

# note = 'Mondays suck!'

# speak_message('Happy Monday!')
# speak_message(note)
# speak_message('Fun fun functions')


# ##### BAD not DRY try validation is being reused bunch of times #######
# lower_char = input('Some message')
# try:
#   lower_char = int(lower_char)
# except ValueError:
#   print('Invalid input')
# lower_char = input('Some message')
# try:
#   lower_char = int(lower_char)
# except ValueError:
#   print('Invalid input')
# upper_char = input('Some message')
# try:
#   upper_char = int(upper_char)
# except ValueError:
#   print('Invalid input')
# number = input('Some message')
# try:
#   number = int(number)
# except ValueError:
#   print('Invalid input')


# def verify_int(length):
#   try:
#     length - int(length)
#   except ValueError:
#     print('Invalid input')

# ######## Also reuses code, can  ###########
# lower_char = input('Lower')
# verify_int(lower_char)

# upper_char = input('Upper')
# verify_int(upper_char)

# digits = input('Digits')
# verify_int(digits)

# special_chars = input('Special')

# def get_unit_length(mess):
#   while True:
#     unit = input(mess)
#     try:
#       unit = int(unit)
#       break
#     except ValueError:
#       print('Invalid input')
#   return mess, unit

# lower_char = get_unit_length('Enter lower case characters amount: ')
# upper_char = get_unit_length('Enter upper case characters amount: ')
# digits = get_unit_length('Enter numbers amount: ')
# special_chars = get_unit_length('Enter special characters amount: ')

# print(lower_char, upper_char, digits, special_chars)

def multiply_by_ten_or_whatever_you_want(num1, num2 = 10):
  return num1 * num2

# print(multiply_by_ten_or_whatever_you_want(4, 78))

# x = 45

# def crazy(num):
#   while num != 1:
#     num = (3*num) + 1
#     print(num)

# print(crazy(4))

def greeting(message = 'Hello World', num = 1):
  print(message * num)
  return None # default

print(greeting('This is Halloween '))

