import random
players = [

]

dice = [
  'L',
  'R',
  'C',
  'd',
  'd',
  'd'
]

# Make player
def add_player():
  while True:
    name = input('Enter name or type "done" when done: ').lower()
    if name == 'done':
      break
    player = {
      'name': name,
      'chips': 3
    }
    players.append(player)

add_player()

# Function to roll dice and return outcome
def roll():
  return random.choice(dice)

# Get number of times we call roll
pot = 0
total_chips = 3 * len(players)
no_winner = True
while no_winner:
  for player in players:
    if player['chips'] == total_chips - pot:
      print(f"Congratulations {player['name']}, You've won {total_chips} chips!")
      no_winner = False
      break
    num_of_rolls = min(player['chips'], 3)
    player_index = players.index(player)
    for _ in range(num_of_rolls):
      outcome = roll()
      player['chips'] -= 1
      if outcome == 'L':
        player_index -= 1
        players[player_index]['chips'] += 1
      elif outcome == 'R':
        player_index += 1
        if player_index == len(players):
          player_index = 0
        players[player_index]['chips'] += 1
      elif outcome == 'C':
        pot += 1
      else:
        player['chips'] += 1


# Contributors
# Tom Hunter, Aaron Parker, Angel Arroyo, DaJuan Martin, Ken Mazur, Gabe Chacon, Anthony Wallace