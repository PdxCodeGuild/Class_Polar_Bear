from django.urls import path

from . import views

app_name = 'url_shortener'

urlpatterns = [
    path('', views.shortener, name='shortener'),
    path('save/', views.save_url, name='save_url'),
    path('<str:code>/', views.redirect, name='redirect')
]

# localhost:8000/shortener/
