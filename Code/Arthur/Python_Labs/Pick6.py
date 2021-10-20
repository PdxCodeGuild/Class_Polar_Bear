'''Pick6
Have the computer play pick6 many times and determine net balance.
Initially the program will pick 6 random numbers as the 'winner'. 
Then try playing pick6 100,000 times, with the ticket cost and payoff below.
A ticket contains 6 numbers, 1 to 99, and the number of matches between 
the ticket and the winning numbers determines the payoff. Order matters, 
if the winning numbers are [5, 10] and your ticket numbers are [10, 5] 
you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket
 numbers are [10, 5, 2], you have 1 match. Calculate your net winnings 
 (the sum of all expenses and earnings).
• a ticket costs $2
• if 1 number matches, you win $4
• if 2 numbers match, you win $7
• if 3 numbers match, you win $100
• if 4 numbers match, you win $50,000
• if 5 numbers match, you win $1,000,000
• if 6 numbers match, you win $25,000,000
One function you might write is pick6() which will generate a list of 6 
random numbers, which can then be used for both the winning numbers and tickets.
Another function could be num_matches(winning, ticket) 
which returns the number of matches between the winning numbers and
 the ticket.
Steps
1. Generate a list of 6 random numbers representing the winning tickets
2. Start your balance at 0
3. Loop 100,000 times, for each loop:
4. Generate a list of 6 random numbers representing the ticket
5. Subtract 2 from your balance (you bought a ticket)
6. Find how many numbers match
7. Add to your balance the winnings from your matches
8. After the loop, print the final balance
Version 2
The ROI (return on investment) is defined as (earnings - expenses)/expenses. 
Calculate your ROI, print it out along with your earnings and expenses'''

import random

def pic6():
  tickets = []
    #initialize an empty list that will be used to store the 6 lucky numbers 
  for x in range(0,6):
    #the computer picks a random number
    number = random.randint(1,99)
    #check if the number has been picked and if it has pick a new number
    while number in tickets:
        number = random.randint(1,99)
    
    #append the number to our list
    tickets.append(number)

    tickets.sort()

  return tickets

def num_matches(winnings, tickets):
     # [89, 88, 75, 34, 20, 19]
    # [90, 88, 4, 34, 99, 19]
    # we check if the numbers at the first index, match the numbers at the second index
    num_matches = 0
    for i in range(len(winnings)):
      if winnings[0] == tickets[0]:
          num_matches = num_matches+1

    return num_matches


# if num_matches == 1:
#     balance +=4
# elif num_matches ==2:
#     balance +=7
# elif num_matches == 3:
#     balance += 100
# elif num_matches == 4:
#     balance +=50000
# elif num_matches == 5:
#     balance +=1000000
# else :
#     balance +=25000000

#we use dictionaries to store the prize and get rid of the if statements
prize = {
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}

winning = pic6()
earnings = 0
expenses =0
#Loop 100,000 times, for each loop:
count = 0
while count < 100000:
    #count +=1
    count =count+1
    #Generating a list of 6 random numbers representing the ticket
    tickets = pic6()
    #Subtract 2 from your balance (you bought a ticket)
    # expenses -= 2
    expenses = expenses-2
    #Find how many numbers match
    num_of_matches = num_matches(winning,tickets)
    #Add to your balance the winnings from your matches
    # earnings += prize.get(num_matches, 0)
    earnings =earnings + prize.get(num_matches,0)
# After the loop, print the final balance
print(f"${earnings - expenses}")
#Version2
print(f"ROI: {(earnings - expenses) / expenses}")
    









       
       
    
    








