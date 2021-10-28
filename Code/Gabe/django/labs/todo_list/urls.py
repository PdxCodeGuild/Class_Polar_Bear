from django.urls import path
from . import views

app_name = 'todo_list'

urlpatterns = [
    # localhost://8000/todo
    path('', views.todo, name='index'),
    # localhost://8000/todo/new
    path('new', views.add_todo, name='add_todo')
]
