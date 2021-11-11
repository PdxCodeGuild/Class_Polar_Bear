from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('\submit', views.save_list, name='save_list'),
]
