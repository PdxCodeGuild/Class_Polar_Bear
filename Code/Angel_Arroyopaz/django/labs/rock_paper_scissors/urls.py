from django.urls import path
from . import views

app_name = 'rock_paper_scissors'

urlpatterns = [
    path('', views.rps, name='rock_paper_scissors')
]