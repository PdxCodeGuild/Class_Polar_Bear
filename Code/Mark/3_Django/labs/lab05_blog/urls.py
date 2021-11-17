from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_post, name='new_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
]

