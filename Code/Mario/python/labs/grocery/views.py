from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .forms import GroceryListForm
from .models import GroceryItem


# Create your views here.


def index(request):
    form = GroceryListForm()
    return render(request, 'index.html', {'form': form})


def save_list(request):
    form = GroceryListForm()
    new_item = GroceryItem()
    item = request.POST['Item']

    if request.method == 'POST':
        user_form = GroceryListForm(request.POST)
        if(user_form.is_valid()):
            new_item.desc = user_form.cleaned_data["Item"]
            new_item.save()
            all_items = GroceryItem.objects.all()  # move out of if block
            return render(request, 'index.html', {'items': all_items, 'form': form})
        else:
            pass
