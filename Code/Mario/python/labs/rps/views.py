from django.shortcuts import render
from django.http import HttpResponse

import random


def main(request):
    return render(request, 'index.html')


def selected(request, choice):
    outcome = ''
    opts = ['rock', 'paper', 'scissors']
    computer = random.choice(opts)

    if choice == computer:
        outcome = "It's a tie"
    elif choice == 'rock' and computer == 'scissors' or choice == 'paper' and computer == 'rock' or choice == 'scissors' and computer == 'paper':
        outcome = 'You win 🎉🎉🎉'
    else:
        outcome = "Computer wins 😈"
    # print(outcome)
    return render(request, 'outcome.html', {
        'outcome': outcome,
        'player': choice,
        'computer': computer
    })
