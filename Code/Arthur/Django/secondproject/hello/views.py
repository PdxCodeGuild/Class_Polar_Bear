from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime


# Create your views here.
def hello(request):
    # return HttpResponse('Hello World!')
    return render(request,'hello/index.html')

def bruce(request):
    # return HttpResponse('Hello Bruce!')
    return render(request,'hello/index.html')

def batman(request):
    # return HttpResponse('Hello Batman!')
    return render(request,'hello/index.html')

#pass a name
def say_hello(request,name):
    # return HttpResponse(f'hello {name}')
    return render(request,'hello/say_hello.html',{'name':name, 'time': datetime.now()})

