from django.http.response import HttpResponse
from django.shortcuts import render
import random
from django import forms    

class NewForm(forms.Form):
    task = forms.CharField(label='Your Selection')

# Create your views here.
def rps(request):
    # list
    list = ["rock", "paper", "scissors"]
    result = ''
    # user input
    if request.method == 'POST':
        form = NewForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data['task']

            user_input = task.lower()

            # computer gets a random choice
            computer = random.choice(list)
            
            # compare
            if user_input == computer:
                result = "It is a tie!"

            elif user_input == "rock":
                if computer == "paper":
                    result = "You lost!"
                elif computer == "scissors":
                    result = "You won!"           

            elif user_input == "paper":
                if computer == "scissors":
                    result = "You lost!"
                elif computer == "rock":
                    result = "You won!"
                    
            elif user_input == "scissors":
                if computer == "rock":
                    result = "You lost!"
                elif computer == "paper":
                    result = "You won!"

    return render(request, 'rock_paper_scissors/main.html', {
        'form': NewForm(),
        'result': result
    })


'''

'''