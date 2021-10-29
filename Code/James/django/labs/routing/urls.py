from django.urls import path
from . import views

urlpatterns = [
    path('routing', views.routing, name='routing'),
    path('animations/', views.animations, name='animations'),
    path('company/', views.company, name='company'),
    path('blog/', views.blog, name='blog'),
    ]