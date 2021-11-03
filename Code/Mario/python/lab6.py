import string
import random

available_char = {
    'special character': string.punctuation,
    'upper_char': string.ascii_uppercase,
    'lower_char': string.ascii_lowercase,
    'numbers': string.digits,
}

generated_password = ''
password_len = 0
overall_size = 0
current_size = 0

while True:
    try:
        password_len = int(
            input('How long would you like your password to be? '))
        for key in available_char:
            if overall_size <= password_len:
                current_size = int(input(f"How many {key}? "))
                overall_size += current_size
                shuffled_char = list(available_char[key])
                random.shuffle(shuffled_char)
                generated_password += ''.join(shuffled_char[:current_size])
            else:  # TODO
                break
            current_size = 0
    except ValueError:
        print('Input must be an integer')
        continue
    t = list(generated_password)
    random.shuffle(t)
    generated_password = ''.join(t)
    break

print(f"Your new password is: {generated_password}")
# while password_len > 0:
#     generated_password += random.choice(password_char)
#     password_len -= 1
# print(generated_password)

# test = list(available_char['special character'])

# random.shuffle(test)
# result = ''.join(test)
# print(result)
