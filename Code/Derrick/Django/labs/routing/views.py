from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def render_bio(request):
    return render(request, 'routing/bio.html', {})

def render_blog(request):
    return render(request, 'routing/blog.html', {})

def render_landingpage(request):
    return render(request, 'routing/landingpage.html', {})

def render_animations(request):
    return render(request, 'routing/animations.html', {})