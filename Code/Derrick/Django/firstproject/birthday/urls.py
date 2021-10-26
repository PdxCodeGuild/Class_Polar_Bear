from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.birthday, name='birthday')
]