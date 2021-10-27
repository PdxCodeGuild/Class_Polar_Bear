from django.shortcuts import render
import random

# Create your views here.
def guess_the_number(request, number):
    computer_choice = random.randit(1, 3)
    return render(request, 'guess_num/index/html', {

    }
    
    )