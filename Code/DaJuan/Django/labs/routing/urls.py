from django.urls import path
from . import views


urlpatterns = [
    path('Bio', views.bio, name='Bio'),
    path('Blog', views.blog, name='blog'),
    path('Store', views.store, name='store'),
]