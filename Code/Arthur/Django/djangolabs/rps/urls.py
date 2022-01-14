from django.urls import path
from . import views


app_name ='rps'

urlpatterns =[
    path('<str:user_choice>',views.rpsfunc,name ='rps')
    
]