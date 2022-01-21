from django.urls import path

from . import views

urlpatterns = [
    path('pokemon/', views.get_pokemon, name="get_pokemon"),
    path('', views.index, name="index")
]
