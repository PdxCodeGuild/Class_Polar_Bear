import random
import string

char_entry = input("How many characters would you like for the password to be?: ")

low_alphas = string.ascii_lowercase
high_alphas = string.ascii_uppercase
numberz = string.digits
symbolz = string.punctuation

elem = low_alphas + high_alphas + numberz + symbolz

product = random.sample(elem, int(char_entry))

password = "".join(product)

print(password)