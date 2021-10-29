from django.urls import path
from . import views

app_name = 'redo_rps'

urlpatterns = [
    path('', views.rps_choice, name='rps_choice'),
    path('rock/', views.rps_rock, name='rps_rock')
]