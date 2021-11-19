from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bio(request):
  return render(request, 'routing/Bio.html')

def blog(request):
  return render(request, 'routing/Blog.html')

def company(request):
  return render(request, 'routing/Company.html')

def animations(request):
  return render(request, 'routing/Animations.html')