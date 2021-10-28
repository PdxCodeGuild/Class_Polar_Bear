from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def render_animations(request):
    return render(request, 'lab01_routing/animations.html', {})

def render_bio(request):
    return render(request, 'lab01_routing/bio.html', {})

def render_blog(request):
    return render(request, 'lab01_routing/blog.html', {})

def render_company(request):
    return render(request, 'lab01_routing/company.html', {})

