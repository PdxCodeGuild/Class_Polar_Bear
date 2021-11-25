from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('bio/', views.bio, name='bio'),
    path('blog/', views.blog, name='blog'),
    path('company/', views.company, name='company'),
    path('animations/', views.animations, name='animations'),
]