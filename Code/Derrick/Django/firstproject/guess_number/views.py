from django.shortcuts import render
from django.http import HttpResponse
import random 

# Create your views here.
def guess(request, num):
    random_num = random.randint(1,3)
    return render(request, 'guess_number/index.html', {
        'num':num,
        'random_num': random_num
    }) 