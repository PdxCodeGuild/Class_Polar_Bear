from django.urls import path
from . import views

urlpatterns=[
    path('', views.todo, name='index'),
    path('new', views.add_todo, name='add_todo')
]