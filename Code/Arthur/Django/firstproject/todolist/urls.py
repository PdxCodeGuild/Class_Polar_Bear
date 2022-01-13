from django.urls import path
from .import views

app_name ='todolist'
urlpatterns =[
      #localhost:8000/todos
    path('',views.todo, name ='index'),
    path('new',views.addtodo, name ='add_todo')
]