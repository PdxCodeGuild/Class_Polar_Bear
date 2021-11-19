#Card Values
    cards = {
        'A' : 11,
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

    hands = {
    'first hand': input('What is your first card'),
    'second hand': input('What is your second card'),
    'third hand': input('What is your third card?')
}
        
        def point_count(hand):
            points = [hand[0] + hand[1] + hand[2]]

            if points > 21 and 'A' in hand:
                points -= 10
            
