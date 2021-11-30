
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms

class NewTodoForm(forms.Form):
    tasks = forms.CharField(label='New Task')

#todos = ['wash the car', 'take out trash', 'water the bird']

# Create your views here.
def todo_list(request):


    if 'todos' not in request.session:
        request.session['todos'] = []

    return render(request, "todolist/index.html", {
        'todos': request.session['todos']
    })

def add_todo(request):
    if request.method == "GET":
        return render(request, 'todolist/add_todo.html',{
        'form' : NewTodoForm
        })

    elif request.method == "POST":

        form = NewTodoForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data['tasks']

            request.session['todos'].append(task)
            request.session.modified = True
            return HttpResponseRedirect(reverse('todolist:todo'))
        #Manual form entry
       # todo = request.POST['todo']
       # todos.append(todo)
        

def remove_todo(request, index):
    request.session['todos'].pop(index)
    request.session.modified = True

    return HttpResponseRedirect(reverse('todolist:todo'))

def clear_items(request):
    request.session['todos'] = []
    request.session.modified = True

    return HttpResponseRedirect(reverse('todolist:todo'))