from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='first'),
    path('second/', views.second, name='second'),
    path('third/<int:item_id>', views.third, name='third'),
]