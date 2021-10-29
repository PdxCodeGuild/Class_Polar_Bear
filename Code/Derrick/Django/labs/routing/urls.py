from django.urls import path
from . import views 

urlpatterns = [
    path('bio/',views.render_bio, name='bio'),
    path('blog/',views.render_blog, name='blog'),
    path('landingpage/',views.render_landingpage, name='landingpage'),
    path('animations/',views.render_animations, name='animations'),        
]