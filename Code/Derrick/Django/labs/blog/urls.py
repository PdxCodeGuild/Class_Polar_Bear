from django.urls import path 
from . import views 

app_name = 'blog'

urlpatterns = [
    path('',views.register,name='index'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('create/',views.create,name='create')
]