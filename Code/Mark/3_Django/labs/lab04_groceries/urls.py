from . import views
from django.urls import path

app_name = 'lab04_groceries'

urlpatterns = [
    path('', views.index, name='index'),
    path('plus/', views.plus, name='plus'),
    path('<int:pk>', views.basket, name='basket')
]

