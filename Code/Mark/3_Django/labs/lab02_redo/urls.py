from django.urls import path
from . import views

app_name = 'lab02_redo'

urlpatterns = [
    path('', views.index, name='index'),
    path('encryption/', views.encryption, name='encryption')
]
