from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name='home_page'),
    path('dashboard/', views.dashboard_page, name='dashboard_page'),
    path('posts/', views.get_posts, name="get_posts"),
]