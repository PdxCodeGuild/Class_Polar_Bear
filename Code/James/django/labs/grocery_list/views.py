from typing import ItemsView
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import GroceryItem
from django.urls import reverse
from . import models



'''
def grocery_list(request):
    return HttpResponse('hello world')
'''

def grocery_list(request):
    grocery_list = models.GroceryItem.objects.all()
    return render(request, 'grocery_list/grocery_list.html', {'grocery_list' : grocery_list})

def input(request):
    item = request.POST['item']
    #item_text = request.POST['item']
    # new_item = models.GroceryItem(item=item_text)
    # new_item.save()
    # return HttpResponseRedirect(reverse('grocery_list:index'))
    status = request.POST['status']
    Grocery_model = GroceryItem(item=item, status=status) # Should grocery_model be GroceryItem?
    Grocery_model.save()
    return HttpResponseRedirect(reverse('myapp:myview'))

def listprint(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'grocery_list/grocery_list.html', context)

def buy_item(request, item_id):
    grocery_item = models.GroceryItem.objects.get(id=item_id)
    grocery_item.completed = not grocery_item.status
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index')) #incomplete 49min

def delete_item(request):
    grocery_item = models.GroceryItem.objects.get(id=item_id)
    grocery_item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))