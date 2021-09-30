import random #<----import random for extra challenge 1


    
grade = input("Enter a test score: ")#<---3.1
numgrade = int(grade)   
opp_score = random.randint(0, 101)#<--Extra challenge 1
difference1 = numgrade - opp_score
difference_low = opp_score - numgrade
# Extra Challenge 2
ext_Chall2 = numgrade % 10

if ext_Chall2 > 4:
    chall2 = "+"
elif  ext_Chall2 == 0:
    chall2 = " "
else:
    chall2 = "-"
#3.2-----
if numgrade > 90:
    print(f"A{chall2}")
elif numgrade > 79  and numgrade < 90:
    print(f"B{chall2}")
elif numgrade > 74 and numgrade < 80:
    print(f"C{chall2}")
elif numgrade > 69 and numgrade < 75:
    print(f"D{chall2}")
elif numgrade < 70:
    print(f"F{chall2}")

if numgrade > opp_score:
    print(f"You beat your rival by {difference1} points!")
    print(f"Your score: {numgrade}....Opp's score: {opp_score}")
elif numgrade == opp_score:
    print("You have tied with your rival!!")
    print(f"Your score: {numgrade}....Opp's score: {opp_score}")
else:
    print(f"Your rival beat you by {difference_low} points...")
    print(f"Your score: {numgrade}....Opp's score: {opp_score}")
    
