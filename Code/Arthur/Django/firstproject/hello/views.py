from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return render(request,'hello/index.html')
    # return HttpResponse('Hello World')

def bruce(request):
    return HttpResponse('Hello Bruce')

def batman(request):
    return HttpResponse('Hello batman')

def say_hello(request,name):
    return render(request,'hello/say_hello.html',{'name':name})
    # return HttpResponse(f'Hello {name}')