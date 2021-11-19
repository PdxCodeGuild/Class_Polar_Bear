from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

import random

# Create your views here.
def guess_the_number(request, number):
  random_num = random.randint(0, 3)
  return render(request, 'guess_num/index.html', {
    'number': number,
    'random_num': random_num
  })
