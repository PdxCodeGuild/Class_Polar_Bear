from django.urls import path
from . import views

# app_name = 'chirp'

urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save_cheep, name='save'),
    path('filter/', views.nono_filter, name='filter')

]