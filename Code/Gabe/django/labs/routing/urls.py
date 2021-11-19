from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('bio', views.bio, name='Bio'),
    path('blog', views.blog, name='Blog'),
    path('company', views.company, name='Company'),
    path('animations', views.animations, name='Animations')
]
