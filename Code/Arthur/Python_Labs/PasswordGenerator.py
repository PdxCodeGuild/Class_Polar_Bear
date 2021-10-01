import random
import string

#ask user to enter the password length 
password_choice = string.printable
while True:
    password_character=""
    password_length =int(input("Enter the length of the password :"))
    for x in range(0,password_length):
        password_character=password_character + random.choice(password_choice)
    print(f"password Generated : {password_character}")


#part2 is for home work
