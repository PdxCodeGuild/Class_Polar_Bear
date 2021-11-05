from django.forms.fields import CharField
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

from .models import GroceryItem, Completed, Incomplete

# Create your views here.

class NewForm(forms.Form):
    grocery = forms.CharField(label='Grocery Item', max_length=25)


def first(request):
    groceries = GroceryItem.objects.all().order_by('id')
    incomplete_items = Incomplete.objects.all().order_by('id')
    completed_items = Completed.objects.all().order_by('id')
    
    return render(request, 'grocery_list/index.html', {
        'groceries':groceries,
        'incomplete_items':incomplete_items,
        'completed_items':completed_items,
        'form':NewForm(),
    })

def second(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        
        if form.is_valid():
            form_grocery = form.cleaned_data['grocery']
            
            grocery_items = GroceryItem()

            grocery_items.item = form_grocery

            grocery_items.save()
    
    return HttpResponseRedirect(reverse('first'))

def third(request, item_id):
    choice = request.GET['choice']

    if choice == 'incomplete':
        grocery_items = GroceryItem.objects.get(id=item_id)
        incomplete_list = Incomplete()
        incomplete_list.incomplete_item = grocery_items
        incomplete_list.save()
        grocery_items.delete()

    elif choice == 'completed':
        grocery_items = GroceryItem.objects.get(id=item_id)
        completed_list = Completed()
        completed_list.completed_item = grocery_items
        completed_list.save()
        grocery_items.delete()   

    elif choice == 'completed_two':
        incomplete_items = Incomplete.objects.get(id=item_id)
        completed_list = Completed()
        completed_list.completed_item = incomplete_items
        completed_list.save()
        incomplete_items.delete()

    elif choice == 'delete':
        grocery_items = GroceryItem.objects.get(id=item_id)
        grocery_items.delete()

    elif choice == 'delete_two':
        incomplete_items = Incomplete.objects.get(id=item_id)
        incomplete_items.delete()

    elif choice == 'delete_three':
        completed_items = Completed.objects.get(id=item_id)
        completed_items.delete()

    return HttpResponseRedirect(reverse('first'))

