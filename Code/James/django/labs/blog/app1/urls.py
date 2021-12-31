from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('mycreate/', views.mycreate, name='mycreate'),
    path('myusercreate/', views.myusercreate, name='myusercreate'),
    path('create/', views.create, name='create'),
    path('login/', views.login, name='login'),
]