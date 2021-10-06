cards = {
    "a" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "j" : 11,
    "q" : 12,
    "k" : 13
}
# print(cards)

card1 = input("Enter your first card: ")
card2 = input("Enter your second card: ")
card3 = input("Enter your third card: ")
# print(card1, card2, card3)

score = cards[card1] + cards[card2] + cards[card3]
# print(score)

if score < 17:
    advice = "Hit"
if score <= 17 and score < 21:
    advice = "Stay"
if score == 21:
    advice = "Blackjack!"
if score > 21:
    advice = "Already Busted"

print(f'{score} {advice}')