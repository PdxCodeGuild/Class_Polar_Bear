from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import models


def index(request):
    grocery_list = models.GroceryItem.objects.all().order_by('department')
    departments = models.Department.objects.all().order_by('name')
    return render(request, 'grocery_list/index.html', {
        'grocery_list': grocery_list,
        'departments': departments
    })

def add_item(request):
    item_text = request.POST['item']
    department_id = request.POST['department']
    new_item = models.GroceryItem()
    new_item.item = item_text
    if department_id:
        department = models.Department.objects.get(id=department_id)
        new_item.department = department
    new_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def buy_item(request, item_id):
    grocery_item = models.GroceryItem.objects.get(id=item_id)
    grocery_item.completed = not grocery_item.completed
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete_item(request, item_id):
    grocery_item = models.GroceryItem.objects.get(id=item_id)
    grocery_item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))
