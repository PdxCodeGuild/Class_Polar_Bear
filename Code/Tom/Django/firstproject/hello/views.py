from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def hello(request):
    return render(request, 'hello/index.html')

def bruce(request):
    return HttpResponse('Hello Bruce')

def batman(request):
    return HttpResponse('Hello Batman')

def say_hello(request, name):
    return render(request, 'hello/say_hello.html', {
        'name':name, 
        'time':datetime.now()
        })