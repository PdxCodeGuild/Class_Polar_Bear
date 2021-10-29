from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('bruce', views.bruce, name='bruce'),
    path('batman', views.batman, name='batman'),
    path('<str:name>', views.say_hello, name='say_hello'),
]