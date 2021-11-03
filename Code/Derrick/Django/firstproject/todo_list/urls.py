from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.todo,name='todos'),
    path('add/',views.add,name='add'),
    path('remove/<int:index>',views.remove,name='remove'),
    path('clear/',views.clear,name='clear')
]