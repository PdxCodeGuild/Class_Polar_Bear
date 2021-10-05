import random

# function definitions
def pick6():
  array = []
  for i in range(6):
    array.append(random.randint(1, 99))
  return array

def num_matches(winning_ticket, ticket):
  count = 0
  for i in range(len(winning_ticket)):
    if winning_ticket[i] == ticket[i]:
      count += 1
  return count

def checker(matches):
  winnings = 0
  if matches == 1:
    winnings = 4
  elif matches == 2:
    winnings = 7
  elif matches == 3:
    winnings = 100
  elif matches == 4:
    winnings = 50000
  elif matches == 5:
    winnings = 1000000
  elif matches == 6:
    winnings = 25000000
  return winnings

# function calls
winner = pick6()

def final_winnings_or_losings():
  balance = 0
  expenses = 0
  earnings = 0
  for time in range(100000):
    balance -= 2
    expenses -= 2
    ticket = pick6()
    current_matches = num_matches(winner, ticket)
    earnings += checker(current_matches)
    balance += checker(current_matches)
    time += 1
  return f'Your final balance is {balance}, and your ROI is {(earnings - expenses) / expenses}.'

print(final_winnings_or_losings())
