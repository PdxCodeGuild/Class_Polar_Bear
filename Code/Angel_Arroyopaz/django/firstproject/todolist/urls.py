from django.urls import path
from . import views

# specify what app to use too pull info from
app_name = 'todolist'

urlpatterns = [
    path('', views.todolist, name='index'),
    path('new', views.add_todo, name='add_todo'),
    path('clear', views.clear_todos, name='clear_todos'),
    path('remove/<int:index>', views.remove_todo, name='remove_todo')
]