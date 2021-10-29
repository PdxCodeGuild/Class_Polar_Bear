from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def routing(request):
    return render(request, 'routing/index.html')

def animations(request):
    return render(request, 'routing/animations.html')

def blog(request):
    return render(request, 'routing/blog.html')

def company(request):
    return render(request, 'routing/company.html')