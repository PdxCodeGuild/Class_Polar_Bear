from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def grading(request):
    # return HttpResponse('hello world!')
    return render(request, 'grading/grading.html')