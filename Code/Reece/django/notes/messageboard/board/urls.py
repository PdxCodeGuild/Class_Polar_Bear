from types import new_class
from django.urls import path
from . import views

app_name ='board'

urlpatterns = [
    path('messageboard/', views.home_page, name='home_page'),
    path('new_message/', views.new_message, name='new_message')
]