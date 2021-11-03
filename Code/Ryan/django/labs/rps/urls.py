from django.urls import path
from . import views

app_name = 'rps'

urlpatterns = [
    path('', views.request_rps, name='request_rps'),
    path('rock', views.choice_rock, name='choice_rock'),
    path('paper', views.choice_paper, name='choice_paper'),
    path('scissors', views.choice_scissors, name='choice_scissors')
]