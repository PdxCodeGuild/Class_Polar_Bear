from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.get_posts, name='get_posts'),
    path('', views.index, name='index')
]
