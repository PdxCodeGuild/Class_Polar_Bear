from django.urls import path
from . import views

urlpatterns = [
    #hello/
    path('', views.hello, name='hello'),
    #hello/bruce
    path('bruce', views.bruce, name='bruce'),
    #hello/batman
    path('batman', views.batman, name='batman'),
    #hello/
    path('<str:name>', views.say_hello, name='say_hello')
]