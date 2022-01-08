from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request, 'rockpaperscissors/index.html')

def result(request):
    user_input=(request.GET['choice'])
    computer_input = random.choice(['rock', 'paper', 'scissors'])
    result = ''
    if user_input=='rock' and computer_input=='scissors':
        result = 'Win!'
    elif user_input=='paper' and computer_input=='rock':
        result = 'Win!'
    elif user_input=='scissors' and computer_input=='paper':
        result = 'Win!'
    elif user_input=='paper' and computer_input=='scissors':
        result = 'Lose!'
    elif user_input=='scissors' and computer_input=='rock':
        result = 'Lose!'
    elif user_input=='rock' and computer_input=='paper':
        result = 'Lose!'
    elif user_input==computer_input: #catches any ties
        result = 'Tie!'
    else: #catches all other results
        result = 'Invalid'

    return render (request, 'rockpaperscissors/results.html', {
        'result':result,
        'user':user_input,
        'computer':computer_input
    })