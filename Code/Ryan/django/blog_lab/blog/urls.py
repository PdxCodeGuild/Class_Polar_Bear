from django.urls import path
from . import views



urlpatterns = [ 
    path('', views.index, name='index'),
    path('new/', views.new_blurb, name='new_blurb'),
    path('delete/<int:blurb_id>', views.delete_blurb, name='delete_blurb'),
    path('reply/<int:blurb_id>', views.reply, name='reply'),
    path('like/<int:blurb_id>', views.like, name='like'),
    path('dislike/<int:blurb_id>', views.dislike, name='dislike'),
    path('detail/<int:blurb_id>', views.detail, name='detail'),
]