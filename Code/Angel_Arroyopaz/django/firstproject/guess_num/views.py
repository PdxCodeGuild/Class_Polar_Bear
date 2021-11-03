from django.http.response import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def guess_the_number(request, number):
    computer_choice = random.randint(0, 5)
    return render(request, 'guess_num/index.html', {
        'number': number,
        'computer_choice': computer_choice,
    })