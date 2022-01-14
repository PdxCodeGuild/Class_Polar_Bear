from django.urls import path
#watch out this is the part that gives alot of errors and django doesn't show
from .import views



urlpatterns =[
    path('',views.hello, name='hello'),
    path('bruce',views.batman, name='bruce'),
    path('batman',views.batman, name='batman'),
    path('<str:name>',views.say_hello,name ='say_hello')
]