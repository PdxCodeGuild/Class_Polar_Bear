from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.
def hello(request): #All functions require 'request' as in user's request.
    return render(request,'hello/index.html')

def bruce(request):
   return HttpResponse('Hello Bruce!')

def batman(request):
    return HttpResponse('Holy smokes, Batman!')

def say_hello(request, name):
    return render(request, 'hello/say_hello.html', {
        'name_key': name, 
        'time_key': datetime.now()
        })