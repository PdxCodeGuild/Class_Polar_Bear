from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def render_animations(request):
    return render(request, 'routing/animations.html', {})

def render_bio(request):
    return render(request, 'routing/bio.html', {})

def render_blog(request):
    return render(request, 'routing/blog.html', {})

def render_landing_page(request):
    return render(request, 'routing/company.html', {})

