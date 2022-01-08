from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('pokemon/', views.pokemon, name='pokemon')
]