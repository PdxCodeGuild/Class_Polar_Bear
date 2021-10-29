from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse
from django.urls import reverse
from django import forms

class NewTodoForm(forms.Form):
    task = forms.CharField(label="To Do")

#todos = ['wash the cat', 'water the bird', 'walk the dog']
# Create your views here.
def todo(request):

    if "todos" not in request.session:
        request.session["todos"] = []

    return render(request, 'todoList/index.html', {
        'todos': request.session['todos']
    })

def add_todo(request):
    if request.method == "GET":
        return render(request, 'todoList/add_todo.html', {
            'form': NewTodoForm()
        })
    elif request.method == "POST":

        form = NewTodoForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data['task']

            #todos.append(task)
            request.session['todos'].append(task)
            # this line lets django know that we want to modify the dictionary as well as the list
            request.session.modified = True
            return HttpResponseRedirect(reverse('todoList:index'))
        else:
            return render(request, 'todoList/add_todo.html', {
                'form': form
            })
        
        #manual way to add to list
        #todo = request.POST['todo']
        #todos.append(todo)

        #return HttpResponse(reverse('todoList:index'))

def remove_todo(request, index):
    request.session['todos'].pop(index)
    request.seeions.modified = True

    return HttpResponseRedirect(reverse('todoList:index'))

def clear_todos(request):
    request.session['todos'] = []
    request.session.modified = True

    return HttpResponseRedirect(reverse('todoList:index'))

