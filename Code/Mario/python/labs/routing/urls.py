from django.urls import path
from . import views

urlpatterns = [
    path('bio', views.bio, name='bio'),
    path('company', views.company, name='company'),
    path('animation', views.animation, name='animation'),
    path('blog', views.blog, name='blog')

]
