import string
import random

chars = string.ascii_lowercase + string.digits

def generate_code():
    code = ''
    for x in range(6):
        code += random.choice(chars)
    return code