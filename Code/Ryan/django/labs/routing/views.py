from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def request_bio(request):
    return render(request, 'bio/index.html')

def request_blog(request):
    return render(request, 'blog/index.html')

def request_company(request):
    return render(request, 'company/index.html')

def request_animations(request):
    return render(request, 'animations/index.html')