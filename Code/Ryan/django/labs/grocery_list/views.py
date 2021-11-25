from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import models

# Create your views here.
def index(request):
    grocery_list = models.GroceryItem.objects.all()
    return render(request, 'grocery_list/index.html', {
        'grocery_list': grocery_list
    })

def add_item(request):
    item_text = request.POST['item']
    new_item = models.GroceryItem(item=item_text)
    new_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def buy_item(request, item_id):
    grocery_item = models.GroceryItem.objects.get(id=item_id)
    grocery_item.completed = not grocery_item.completed
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete_item(reqeust, item_id):
    grocery_item = models.GroceryItem.objects.get(id=item_id)
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

