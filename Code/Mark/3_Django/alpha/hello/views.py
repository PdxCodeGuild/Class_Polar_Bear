from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'hello/index.html')

def say_hello(request, name):
    return render(request,'hello/say_hello.html', {'name':name, 'time':datetime.now()})

def say_hello_to_name(request, name):
    return HttpResponse(f'Hello {name}!')

