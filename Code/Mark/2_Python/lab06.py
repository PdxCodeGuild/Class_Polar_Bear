import random, string
alphabet = string.ascii_letters + string.digits + string.punctuation
password = str()
while len(password) < 10:
    password += random.choice(alphabet)
print('Your password:', password)

