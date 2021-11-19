from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from django import forms
import random

class NewGame(forms.Form):
    task = forms.CharField(label="Choice")

def request_rps(request):
    return render(request, 'rps/index.html')

def choice_rock(request):
    if request.method == "POST":
        human_choice = 'rock'
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        if human_choice == computer_choice:
            result = 'You have tied!'
        elif computer_choice == 'paper':
            result = 'You lost'
        else:
            result = 'You win' 
            request.session.modified = True
        # prints to cmd prompt
        print(human_choice, computer_choice, result)
        
        return render(request, 'rps/played.html', {
        'choice': human_choice, 'computer': computer_choice, 'result': result
    })

def choice_paper(request):
    if request.method == "POST":
        human_choice = 'paper'
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        if human_choice == computer_choice:
            result = 'You have tied!'
        elif computer_choice == 'scissors':
            result = 'You lost'
        else:
            result = 'You win' 
            request.session.modified = True
        # prints to cmd prompt
        print(human_choice, computer_choice, result)
        return render(request, 'rps/played.html', {
        'choice': human_choice, 'computer': computer_choice, 'result': result
    })

def choice_scissors(request):
    if request.method == "POST":
        human_choice = 'scissors'
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        if human_choice == computer_choice:
            result = 'You have tied!'
        elif computer_choice == 'rock':
            result = 'You lost'
        else:
            result = 'You win' 
            request.session.modified = True
        # prints to cmd prompt
        print(human_choice, computer_choice, result)
        return render(request, 'rps/played.html', {
        'choice': human_choice, 'computer': computer_choice, 'result': result
    })