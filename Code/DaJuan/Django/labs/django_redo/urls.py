from django.urls import path
from . import views

app_name = 'django_redo'

urlpatterns = [
    path('', views.user_pick, name='user_pick'),
    path('rock', views.rock, name='rock'),
    path('paper', views.paper, name='paper'),
    path('scissors', views.scissors, name='scissors'),
]