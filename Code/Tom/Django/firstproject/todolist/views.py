from django.shortcuts import render

# Create your views here.

todos = ['wash the cat', 'water the bird', 'walk the dog']

app_name='todolist'

def todo(request):
    return render(request, 'todolist/index.html', {
        'todos':todo
    })

def add_todo(request):
    return render(request, 'todolist/add_todo.html')