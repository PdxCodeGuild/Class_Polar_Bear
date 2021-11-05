from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'rps/index.html')

def result(request):
    choice=request.GET['choice']
    computer = random.choice(['rock', 'paper', 'scissors'])
    result = ''
    if choice == computer:
        result = 'You tied'
    elif choice == 'rock':
        if computer == 'paper':
            result = "You lost."
        else:
            result = "You won!"
    elif choice == 'paper':
        if computer == 'scissors':
            result = "You lost."
        else:
            result = "You won!"
    elif choice == 'scissors':
        if computer == 'rock':
            result = "You lost."
        else:
            result = "You won!"
    return render(request, 'rps/results.html', {
        'result': result
        })