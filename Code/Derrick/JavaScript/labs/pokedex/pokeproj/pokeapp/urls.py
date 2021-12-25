from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home_page,name='home'),
    path('pokemon/',views.get_pokemon, name='get_pokemon'),
]