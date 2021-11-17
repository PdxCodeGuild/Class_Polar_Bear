from django.urls import path
from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('grocery_list/', views.grocery_list, name='grocery_list'),
    path('grocery_list/', views.input, name='input'),
    path('grocery_list/', views.listprint, name='listprint'),
]