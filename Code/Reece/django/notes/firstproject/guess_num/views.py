from django.shortcuts import render
from django.http import HttpResponse

import random

# Create your views here.
def guess_the_number(request, number):
    computer_choice = random.randint(1, 3)
    return render(request, 'guess_num/index.html', {
        'number': number,
        'computer_choice': computer_choice
    })
