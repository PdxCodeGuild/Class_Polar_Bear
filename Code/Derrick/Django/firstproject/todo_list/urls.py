from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.todo,name='todos'),
    path('add/',views.add,name='add')
]