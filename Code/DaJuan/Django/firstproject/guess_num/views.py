from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def guess_the_num(requests, num):
    computer_choice = random.randint(1, 3)
    return render(requests, 'guess_num/index.html', {
        'num': num,
        'computer_choice' : computer_choice,
    })
    