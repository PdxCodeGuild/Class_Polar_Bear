from django.urls import path 
from . import views


urlpatterns = [
    path('<int:num>', views.guess_the_num, name='guess')
]