from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .import models
# from New_Polar.Code.Arthur.Django.djangolabs import grocerylist



# Create your views here.
def index(request):
    grocerylist = models.GroceryItem.objects.all()
    return render(request,'grocerylist/index.html',{
        'grocerylist' : grocerylist
    })


#logic where our items should go
def add_grocery(request):
    item_grocery =request.POST['item']
    new_item =models.GroceryItem(item=item_grocery)
    new_item.save()
    return HttpResponsePermanentRedirect(reverse('grocerylist:index'))

def check_grocery(request,item_id):
    grocery_item = models.GroceryItem.objects.get(id=item_id)
    grocery_item.completed = True
    grocery_item.save()
    return HttpResponsePermanentRedirect(reverse('grocerylist:index'))



