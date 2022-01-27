from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.get_posts, name='get_posts')
]