from datetime import datetime, timezone
from django.utils import timezone
from django.forms import fields
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import GroceryItem
from django.db.models import F

from grocery_list.models import GroceryItem


class NewItemForm(forms.Form):
    item_text = forms.CharField(label='Add item')


class MarkComplete(forms.Form):
    mark_complete = fields.BooleanField(initial=False)


class MarkIncomplete(forms.Form):
    mark_incomplete = fields.BooleanField(initial=True)

# Create your views here.


def index(request):
    incomplete_list = GroceryItem.objects.filter(
        is_complete=False).order_by('-date_added')
    completed_list = GroceryItem.objects.filter(
        is_complete=True).order_by('-date_added')
    deleted_list = GroceryItem.objects.filter(
        deleted=True).order_by('-date_added')
    return render(request, 'grocery_list/index.html', {
        'incomplete_list': incomplete_list,
        'completed_list': completed_list,
        'deleted_list': deleted_list,
        'addItem': NewItemForm(),
        'markCompleteForm': MarkComplete(),
        'markIncompleteForm': MarkIncomplete(),
    })


def add_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST)

        if form.is_valid():
            form_item = form.cleaned_data['item_text']

            addGrocery = GroceryItem()
            addGrocery.item_text = form_item
            addGrocery.is_complete = False
            addGrocery.deleted = False
            addGrocery.date_added = timezone.now()

            addGrocery.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))


def mark_complete(request):
    if request.method == 'POST':
        form = MarkComplete(request.POST)
        print(form)
        form_com = form.cleaned_data['mark_complete']
        print(form_com)
        updateGroceryStatus = GroceryItem()
        updateGroceryStatus.is_complete = True

        updateGroceryStatus.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))


def mark_incomplete(request):
    if request.method == 'UPDATE':
        form = MarkComplete(request.UPDATE)
        print(form)
        if form.is_valid():
            form = form.cleaned_data['mark_incomplete']
            print(form)
            updateGroceryStatus = GroceryItem()
            updateGroceryStatus.is_complete = form

            updateGroceryStatus.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))
