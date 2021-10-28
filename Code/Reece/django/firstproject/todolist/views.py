from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


todos = ['wash the cat', 'water the bird', 'walk the dog']

# Create your views here.
def todo(request):
    return render(request, 'todolist/index.html', {
        'todos': todos
    })

def add_todo(request):
    if request.method == "GET":
        return render(request, 'todolist/add_todo.html')
    elif request.method == "POST":

        todo = request.POST['todo']
        todos.append(todo)

        return HttpResponseRedirect(reverse('todolist:index'))