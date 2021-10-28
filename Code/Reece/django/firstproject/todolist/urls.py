
from django.urls import path
from . import views

urlspatterns = [
    path('', views.todo, name='index')
]