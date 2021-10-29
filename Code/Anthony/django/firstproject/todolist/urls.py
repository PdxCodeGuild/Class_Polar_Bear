
from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns = [
    # localhost:8000/todos
    path('', views.todo, name='index'),
    # localhost:8000/todos/new
    path('new', views.add_todo, name='add_todo'),
    # localhost:8000/todos/remove/0
    path('remove/<int:index>', views.remove_todo, name='remove_todo'),
    path('clear', views.clear_todos, name='clear_todos')
]