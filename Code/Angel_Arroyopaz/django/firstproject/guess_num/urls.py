from django.urls import path
from . import views

urlpatterns = [
    path('<int:number>', views.guess_the_number, name='guess')
]