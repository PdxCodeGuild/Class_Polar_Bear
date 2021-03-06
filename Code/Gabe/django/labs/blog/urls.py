from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('create/', views.create_post, name='create'),
    path('edit/<str:blogpost_id>', views.edit, name='edit'),
    path('posts/<int:id>', views.posts, name='posts'),
    path('detail/<int:post_id>', views.detail, name='detail')
]
