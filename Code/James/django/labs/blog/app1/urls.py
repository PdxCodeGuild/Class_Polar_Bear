from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('mycreate/', views.mycreate, name='mycreate'),
    path('create/', views.create, name='create'),
    path('mylogin/', views.mylogin, name='mylogin'),
]