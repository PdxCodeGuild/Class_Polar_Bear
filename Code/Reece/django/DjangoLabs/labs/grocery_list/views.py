from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import GroceryItem

def index(request):
    grocery_list = GroceryItem.objects.all()
    return render(request, 'grocery_list/index.html', {
        'grocery_list':grocery_list
    })

def add_item(request):
    item_text = request.POST['item']
    new_item = GroceryItem()
    new_item.item = item_text
    new_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def completed(request, item_id):
    grocery_item = get_object_or_404(GroceryItem, id=item_id)
    grocery_item.completed = not grocery_item.completed
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete_item(request, item_id):
    grocery_item = get_object_or_404(GroceryItem, id=item_id)
    grocery_item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))