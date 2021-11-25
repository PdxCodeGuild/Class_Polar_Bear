from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.todo_list, name='todo'),
    path('add', views.add_todo, name='add')
]