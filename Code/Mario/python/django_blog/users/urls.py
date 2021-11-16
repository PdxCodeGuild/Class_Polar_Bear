from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.user_login, name='user_login'),
    path('welcome', views.welcome, name='welcome'),

]
