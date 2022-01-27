from django.urls import path

from . import views

urlpatterns =[
    path('<int:number>', views.guess_number, name = 'guess')
]