# Black Jack advice

deck  = {
    'A' : 1,
     '2' : 2,
     '3' : 3,
     '4' : 4,
     '5' : 5,
     '6' : 6,
     '7' : 7,
     '8' : 8,
     '9' : 9,
     '10' : 10,
     'J' : 10,
     'Q' : 10,
     'K' : 10
}

# ask the user for 3 playing cards

first_card = input('Whats your first card? ')
second_card = input('Whats your second card? ')
third_card = input('Whats your third card? ')

# Take all three inputs, compare to the deck, and store in a list
input_cards = []
def cards(x):
    # while True:
        if x in deck.keys():
            input_cards.append(x)
            print(input_cards)
        
        else:
            print ('Enter a valid card')
        
#  get the sum of the indeces of input_cards
...



cards(first_card)
cards(second_card)
cards(third_card)













# second()
# third()

# put_cards = []
# def cards(x, y, z):
#     x == first_card
#     y == second_card
#     z == third_card
#     if x in card_value.keys():
#         input_cards.append([x, y, z])
#         print(input_cards)
#     else:
#         print ('Enter a valid card')
#     return x, y, z



# cards(first_card, second_card, third_card)





# def second():
#     if second_card in cards.keys():
#         input_cards.append(second_card)
#     else:
#         print ('Enter a valid card')
#     return input_cards

# def third():
#     if third_card in cards.keys():
#         input_cards.append(third_card)
#     else:
#         print ('Enter a valid card')
#     return input_cards
