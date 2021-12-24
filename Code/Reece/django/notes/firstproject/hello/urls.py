from django.urls import path
from . import views


urlpatterns = [
    # hello/
    path('', views.hello, name='index'),
    # hello/bruce
    path('bruce', views.bruce, name='bruce'),
    path('batman', views.batman, name='batman'),
    path('<str:name>', views.say_hello, name='say_hello')
]