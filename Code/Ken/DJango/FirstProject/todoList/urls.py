from django.urls import path
from . import views

urlpatterns = [
    #localhost:8000/todo
    path('', views.todo, name='index'),
    #todo/new
    path('new', views.add_todo, name='add_todo'),
    #localhost:8000/todos/remove/1 - 1 being the index location
    path('remove/<int:index>', views.remove_todo, name='remove_todo'),
    path('clear', views.views.clear_todos, name='clear_todos')
]