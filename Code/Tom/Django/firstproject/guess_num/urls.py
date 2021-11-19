from django.urls import path
from . import views

urlpatterns = [
    #hello/
    path('<int:number>', views.guess_the_number, name='number'),
    ]