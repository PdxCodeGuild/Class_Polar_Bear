from django.shortcuts import get_object_or_404, render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import GroceryItem
# Create your views here.

class NewForm(forms.Form):
    text = forms.CharField(label='Item', max_length=50)
    completed = forms.BooleanField(label='Completed',required=False)

def render_grocery_list(request):
    groceries = GroceryItem.objects.all()
    return render(request, 'grocery_list/index.html',{'form': NewForm(),'groceries': groceries})

def update_list(request):
    form = NewForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            grocery_text = form.cleaned_data['text']
            grocery_completed = form.cleaned_data['completed']
            grocery = GroceryItem()
            grocery.text = grocery_text
            grocery.completed = grocery_completed
            grocery.save()
        return HttpResponseRedirect(reverse('grocery_list'))
        # return render(request, 'grocery_list/index.html',{'form': NewForm(),'groceries': groceries})

def remove_item(request,g_id):
    g = GroceryItem.objects.get(pk=g_id)
    g.delete()
    return HttpResponseRedirect(reverse('grocery_list'))

def mark_completed(request,g_id):
    g = GroceryItem.objects.get(pk=g_id)
    g.completed = 1
    g.save()
    return HttpResponseRedirect(reverse('grocery_list'))
