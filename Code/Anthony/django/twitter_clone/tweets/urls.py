from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new_tweet, name='new_tweet'),
    # path('delete/', views.delete_tweet, name='delete_tweet'),
    # path('reply/', views.reply, name='reply'),
    # path('like/', views.like, name='like'),
    # path('dislike/', views.dislike, name='dislike'),
    # path('detail/', views.detail, name='detail'),
    # path('report/', views.report, name='report'),
]