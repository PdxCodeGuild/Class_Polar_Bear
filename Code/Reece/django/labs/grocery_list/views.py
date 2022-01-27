from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import Item
# Create your views here.

def GroceryItems(request):
    grocery_items = Item.objects.all()
    context = {
        'grocery_items':grocery_items
    }
    return render(request, 'grocery_list/index.html', context)

def add_item(request):
    if request.method == 'GET':
        return render(request, 'todolist/index.html', {
            'form'
        })

# def add_item(request):
#     input_field1 = request.POST('input_field')
#     # additem = AddItem(item=input_field1)
#     additem = Item()
#     additem.save()
#     return HttpResponseRedirect(reverse('add_item'))
#     # return render(request, 'grocery_list/index.html')