from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.get_posts, name='get_posts'),
    path('save_post/', views.save_post, name='save_post'),
    path('', views.index, name='index')
]