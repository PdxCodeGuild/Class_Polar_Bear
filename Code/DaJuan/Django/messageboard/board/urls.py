from django.urls import path
from . import views

urlpatterns = [
    path('messageboard/', views.home, name='home'),
    path('new_message/', views.new_message, name='new_message')
]