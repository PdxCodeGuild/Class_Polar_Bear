from django.urls import path
from .import views

urlpatterns = {
    #hello/
    path('hello',views.hello, name ='hello'),
    #hello bruce
    path('bruce', views.bruce, name ='bruce'),
    path('batman', views.batman, name ='batman'),
    #pass in the same as the name
    path('<str:name>', views.say_hello, name ='say_hello')
}