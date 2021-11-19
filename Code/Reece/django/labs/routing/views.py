from django.shortcuts import render
from django.http import HttpResponse
from django.utils.regex_helper import flatten_result

# Create your views here.
def routing(request):
    # return render(request, )
    return HttpResponse('Hello...Routing')

def number(request, num):
    context = {'num':num}
    return render(request, 'routing/index.html', context)

def bf_bio(request):
    return render(request, 'routing/bf_bio.html')

def blog(request):
    return render(request, 'routing/blog.html')

def reeces_pizza(request):
    return render(request, 'routing/reeces_pizza.html')

def buttons(request):
    return render(request, 'routing/buttons.html')