from os import putenv, stat
from django.http.response import HttpResponse
from django.shortcuts import render
# from datetime import datetime
from django.http import HttpResponse, request

# Create your views here.

def hello(request):
    return HttpResponse("hello world")

def batman(request):
    return HttpResponse("Hello Batman")

def bruce(request):
    return HttpResponse("Hello Bruce")

def say_hello(request,name):
    return HttpResponse(f'hello {name}')

# #for future notes
# # def say_hello(request,name):
# return render(request,'hello/say_hello.html',{'name':name})
# then on the html page you put
# <h1> hello {{name}</h1>}

# #for future notes
# # def say_hello(request,name):
# return render(request,'hello/say_hello.html',{'name':name,
# 'time':time.now()})
# then on the html page you put
# <h1> hello {{name}}</h1>
# <h3> current time is {{time}}

#to add styling add
# {%load static%}