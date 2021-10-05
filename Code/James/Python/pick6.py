'''
___________________________________________________________________________
Project: Full Stack Evening Boot Camp - Python Lab (08 Pick6)
    Version: 1.0
Author: James Thornton
  Email: James.ed.thornton@gmail.com
Date: 4 OCT 2021
___________________________________________________________________________
'''

import random

'''
computer = []
for i in range(0,6):
    x = random.randint(0,99)
    computer.append(x)
'''

# print(computer)

'''
pick = []
for i in range(0,6):
    x = random.randint(0,99)
    pick.append(x)
# print(pick)
'''


def pick6(list):
  i = 0
  for i in range(0,6):
      x = random.randint(0,99)
      list.append(x)
      i += 0
  return list


def match_count(auto, generated):
  counter = 0
  if auto[0] == generated[0]:
    counter +=1
  if auto[1] == generated[1]:
    counter +=1
  if auto[2] == generated[2]:
    counter +=1
  if auto[3] == generated[3]:
    counter +=1
  if auto[4] == generated[4]:
    counter +=1
  if auto[5] == generated[5]:
    counter +=1
  return counter

'''
list10 = [1,2,3,4,5,6]
list11 = [1,2,3,4,5,6]
print(match_count(list10, list11), "match count")
'''

def winning(match_number):
  winnings = 0
  if match_number == 1:
    winnings += 4
  if match_number == 2:
    winnings += 7
  if match_number == 3:
    winnings += 100
  if match_number == 4:
    winnings += 50
  if match_number == 5:
    winnings += 1000000
  if match_number == 6:
    winnings += 25000000
  return winnings  

# print(winning(2), "winning2")

# list3 = []
# print(pick6(list3))

c = 0
winner = pick6([])
balance = 0
while c < 100000:
  pick = pick6([])
  c += 1
  balance -= 2
  matches = int(match_count(winner, pick))
  balance += int(winning(matches))

print(f'Your balance is ${balance}')
print(winner, "winner")

def ROI(balance2, expenses2):
  value = balance2 * 100/expenses2
  return value

expenses1 = 2 *100000

print(f'{ROI(balance, expenses1)}% is your ROI')