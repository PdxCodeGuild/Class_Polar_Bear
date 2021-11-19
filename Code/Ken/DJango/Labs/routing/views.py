from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Bio(request):
    return render(request, 'routing/Bio.html')

def Blog(request):
    return render(request, 'routing/Blog.html')

def Animations(request):
    return render(request, 'routing/Animations.html')

def Company(request):
    return render(request, 'routing/tomshardware.html')
