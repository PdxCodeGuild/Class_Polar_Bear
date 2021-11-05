from . import models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

def index(request):
    grocery_todo = models.Grocery.objects.filter(is_complete=False)
    grocery_done = models.Grocery.objects.filter(is_complete=True)
    context = {
        'grocery_todo': grocery_todo,
        'grocery_done': grocery_done,
    }
    return render(request, 'lab04_groceries/index.html', context)

def plus(request):
    test = request.POST['grocery']
    test = models.Grocery(grocery=test)
    test.save()
    return HttpResponseRedirect(reverse('lab04_groceries:index'))

