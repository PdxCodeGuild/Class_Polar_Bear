import random

counter = 0
computer = int(input("Pick a number between 1 & 10: "))

current_guess = ""
last_guess = ""
guess = False
diff_message = ""


while True:
    user_input = random.randint(1,10)

    # try:
    #     user_input = int(user_input)
    # except ValueError: 
    #     print("Invalid number try again.")
    #     counter += 1
    #     continue
    # if user_input > 10:
    #     print("Number must be between 1 & 10.")
    #     counter += 1
    #     continue
    # elif user_input < 1:
    #     print("Number must be between 1 & 10.")
    #     counter += 1
    #     continue
        
    
    if user_input == computer:
        counter += 1
        print(f"{user_input} was correct! It took you {counter} attempts.")
        break
    else:
        current_guess = user_input
        if guess == True:
            curr_dif = abs(current_guess - computer)
            # print(curr_dif)
            last_dif = abs(last_guess - computer)
            if curr_dif < last_dif:
                diff_message = f" Your guess of {current_guess} is closer to the target number."
            elif last_dif < curr_dif:
                diff_message = f" Your guess of {current_guess} is farther from the target number."
            else:
                diff_message = f" Your guess of {current_guess} is the same distance from target number."

        if user_input < computer:
            print(f"{user_input} is too low.{diff_message}")
        else:
            print(f"{user_input} is too high.{diff_message}")
        counter += 1    
        last_guess = user_input
        guess = True