from django.urls import path
from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.grocery_list, name='grocery_list'),
    path('grocery_list/', views.input, name='input'),
    path('buy/<int:item_id>/', views.buy_item, name='buy'),
    path('delete/<int:item_id>/', views.delete_item, name='delete'),
]