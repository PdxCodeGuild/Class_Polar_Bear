from django.urls import path 
from . import views 

app_name = 'blog'

urlpatterns = [
    path('',views.register,name='index'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.register,name='register'),
    path('edit/<int:post_id>',views.edit,name='edit'),
    path('create/',views.create,name='create'),
    path('posts/',views.posts,name='posts'),
    path('posts/<int:post_id>',views.details,name='details')

]