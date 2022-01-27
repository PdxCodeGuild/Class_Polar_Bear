from django.http.response import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def guess_number(request, number):
    #pick a number between 0 and 10
    computer_choice = random.randint(0,10)
    # if number == computer_choice:
    #     return HttpResponse(f"you guessed the numbber {number} correctly")
    # else:
    #     return HttpResponse(f"You did not guess number {number} wrong")
    return render(request, 'guess_number/index.html',{
        'number' : number,
        'computer_choice': computer_choice
    })
