from django.contrib import admin
from django.urls import path, include

from grocery_list.models import Item
from . import views

urlpatterns = [
    path('', views.GroceryItems, name='index'),
    path('add_item/', views.add_item, name='add_item'),
]