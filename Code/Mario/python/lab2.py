import random
import os
import time
def clear(): return os.system('cls')


opts = ['rock', 'paper', 'scissors']
play_again = True

while play_again:
    user = input("Rock, Paper or Scissors?: ").lower()
    computer = random.choice(opts)
    clear()
    print(f"Computer: {computer}\nUser: {user}")
    print('\n')
    if user == computer:
        print("It's a tie")
    elif user == 'rock' and computer == 'scissors' or user == 'paper' and computer == 'rock' or user == 'scissors' and computer == 'paper':
        print('You win 🎉🎉🎉')
    else:
        print("Computer wins 😈")
    replay = input("Play again? Y or N: ").lower()
    if replay == 'y':
        print('👍')
        time.sleep(.8)
        clear()
        continue
    break
print("Goodbye! 🙄")
