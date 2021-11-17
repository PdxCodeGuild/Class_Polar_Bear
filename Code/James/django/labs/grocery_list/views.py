from typing import ItemsView
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import GroceryItem

'''
def grocery_list(request):
    return HttpResponse('hello world')
'''

def grocery_list(request):
    groceries = GroceryItem.objects.all()
    context = {
        'groceries' : groceries
    }
    return render(request, 'grocery_list/grocery_list.html', context)

def input(request):
    item = request.POST['item']
    status = request.POST['status']
    Grocery_model = GroceryItem(item=item, status=status) # Should grocery_model be GroceryItem?
    Grocery_model.save()
    return HttpResponseRedirect(reverse('myapp:myview'))

def listprint(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'grocery_list/grocery_list.html', context)