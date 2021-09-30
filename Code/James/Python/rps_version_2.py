'''
___________________________________________________________________________
Project: Full Stack Evening Boot Camp - Python Lab (05 Rock Paper Scissors)
    Version: 1.0
Author: James Thornton
  Email: James.ed.thornton@gmail.com
Date: 27 SEP 2021
___________________________________________________________________________
'''

import random  

options = ["rock", "paper", "scissors"]

while True:
  comp = random.choice(options)
  user = ""
  while user not in options:
    user = input("Pick 'rock', 'paper', or 'scissors': ").lower()
    if user == "exit":
      break
  if user == "exit":
      break
  if user == comp: 
    print("You tied!") 
  elif user == "rock": 
    if comp == "scissors":
      print("You win!")
    elif comp == "paper":
      print("You lose!")
  elif user == "paper":
    if comp == "rock": 
      print("You win!")
    elif comp == "scissors":
      print("You lose!")
  elif user == "scissors":
    if comp == "paper":
      print("You win!")
    elif comp == "rock":
      print("You lose!") 
  user2 = input("would you like to play again: ")
  if user2 == "yes":
    continue
  if user2 == "no":
    quit() 

