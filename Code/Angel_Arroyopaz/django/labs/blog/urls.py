from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),    
    path('create/', views.create, name='create'),
    path('edit/<int:blogpost_id>/', views.blog_edit, name='blog_edit'),
    path('details/<int:blogpost_id>/', views.details, name='details'),
]