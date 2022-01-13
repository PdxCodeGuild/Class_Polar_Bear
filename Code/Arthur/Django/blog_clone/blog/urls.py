from django.urls import path
from .import views


urlpatterns =[
    path('', views.index, name ='index'),
    path('new/', views.new_blog, name ='new_blog'),
    # path('delete/', views.delete_blog, name ='delete_blog'),
    # path('reply/', views.reply, name ='reply'),
    # path('like/', views.like, name ='like'),
    # path('detail/', views.detail, name ='detail'),
    # path('report/', views.report, name ='report'),


]