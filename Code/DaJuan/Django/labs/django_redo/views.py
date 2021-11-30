from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
import random

# Create your views here.
choices = ['rock', 'paper', 'scissors']


def user_pick(requests):
    return render(requests, 'django_redo/user_pick.html')

def rock(requests):
    computer_selection = random.choice(choices)
    return render(requests, 'django_redo/rock.html', {
        'computer_selection': computer_selection
    })

def paper(requests):
    computer_selection = random.choice(choices)
    return render(requests, 'django_redo/paper.html', {
        'computer_selection': computer_selection
    })         
    
def scissors(requests):
    computer_selection = random.choice(choices)
    return render(requests, 'django_redo/scissors.html', {
        'computer_selection': computer_selection
    })


