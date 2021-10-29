from django.urls import path
from . import views

app_name = 'rot_cipher'

urlpatterns = [
    path('', views.rot_cipher, name='index'),
    path('cypher word/', views.cipher_word, name='cipher_word'),
    path('remove/<int:index>', views.remove_word, name='remove'),
    path('clear', views.clear, name='clear')
]
