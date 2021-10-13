playing_cards = {
  'A': 1,
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  '10': 10,
  'J': 10,
  'Q': 10,
  'K': 10
}

def add_up(card1, card2, card3):
  count = 0
  result = playing_cards[card1] + playing_cards[card2] + playing_cards[card3]
  numsList = [playing_cards[card1], playing_cards[card2], playing_cards[card3]]
  for i in numsList:
    if i == 1:
      count+=1
  if count > 1:
    if result + 10 <= 21:
      result+=10
  return result

def verify_input(card):
  if playing_cards.get(card) == None:
    return False
  return True

while True:
  first_card = input("\nWhat's your first card? ").upper()
  second_card = input("What's your second card? ").upper()
  third_card = input("What's your third card? ").upper()

  if not verify_input(first_card) or not verify_input(second_card) or not verify_input(third_card):
    print('\nInvalid card, please try again...')
    break
  if add_up(first_card, second_card, third_card) < 17:
    print('\nHit')
    break
  elif add_up(first_card, second_card, third_card) >= 17 and add_up(first_card, second_card, third_card) < 21:
    print('\nStay')
    break
  elif add_up(first_card, second_card, third_card) == 21:
    print('\nBlackjack!')
    break
  else:
    print('\nAlready Busted')
    break