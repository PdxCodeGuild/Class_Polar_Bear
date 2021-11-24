from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def bio(requests):
    return render(requests, 'routing/Lab01_Bio.html')

def blog(requests):
    return render(requests, 'routing/Lab02_Blog.html')

def store(requests):
    return render(requests, 'routing/Lab3.html')