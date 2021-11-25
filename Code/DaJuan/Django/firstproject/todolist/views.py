
from django.shortcuts import render
from django.http import HttpResponse


todos = ['wash the car', 'take out trash', 'water the bird']

# Create your views here.
def todo_list(request):
    return render(request, "todolist/index.html", {
        'todos': todos
    })

def add_todo(request):
    if request.method == "GET":
        return render(request, 'todolist/add_todo.html')
    if request.method == "POST":
        todo = request.POST['todo']
        todos.append(todo)
        return HttpResponse('Post Accepted.')