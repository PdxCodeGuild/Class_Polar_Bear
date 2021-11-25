from typing import ItemsView
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import GroceryItem
from django.urls import reverse
from . import models

def grocery_list(request):
    grocery_list = models.GroceryItem.objects.all()
    return render(request, 'grocery_list/grocery_list.html', {'grocery_list':grocery_list})

def input(request):
    item_text = request.POST['item']
    new_item = models.GroceryItem()
    new_item.item = item_text
    new_item.save()
    print(request.POST)
    return HttpResponseRedirect(reverse('grocery_list:grocery_list'))

def buy_item(request, item_id):
    grocery_item = models.GroceryItem.objects.get(id=item_id)
    grocery_item.status = not grocery_item.status
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:grocery_list')) #incomplete?

def delete_item(request, item_id):
    grocery_item = models.GroceryItem.objects.get(id=item_id)
    grocery_item.delete()
    return HttpResponseRedirect(reverse('grocery_list:grocery_list')) # index?