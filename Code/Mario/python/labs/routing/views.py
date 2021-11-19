from django.shortcuts import render
from django.http import HttpResponse


def bio(request):
    return render(request, 'bio.html')


def animation(request):
    return render(request, 'animation.html')


def blog(request):
    return render(request, 'blog.html')


def company(request):
    return render(request, 'company.html')
