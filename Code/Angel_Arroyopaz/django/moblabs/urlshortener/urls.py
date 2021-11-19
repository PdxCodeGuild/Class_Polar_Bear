from collections import namedtuple
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shortener, name='shortener'),
    path('save', views.save_url, name='save_url'),
    path('<str:code>', views.url_redirect, name='url_redirect'),
]