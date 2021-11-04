from django.urls import path
from . import views 

urlpatterns = [
    path('message_board/', views.render_board, name='message_board'),
    path('send_message/', views.send_message, name='send_message')   
]