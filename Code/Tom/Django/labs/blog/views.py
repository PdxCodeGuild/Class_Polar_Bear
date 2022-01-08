from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'blog/index.html')

def login(request):
    return render(request, 'blog/login.html')

def logout(request):
    return render(request, 'blog/logout.html')

def profile(request):
    return render(request, 'blog/profile.html')
