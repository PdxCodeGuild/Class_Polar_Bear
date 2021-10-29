from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms

class NewTodoForm(forms.Form):
    task = forms.CharField(label='Todo')

# Create your views here.
def todo(request):

    if "todos" not in request.session:
        request.session["todos"] = []

    return render(request, 'todolist/index.html', {
        'todos': request.session["todos"]
    })

def add_todo(request):
    if request.method == "GET":
        return render(request, 'todolist/add_todo.html', {
            'form': NewTodoForm()
        })

    elif request.method == "POST":

        form =NewTodoForm(request.POST)

        if form.is_valid():
            request.session.modified =True
            task = form.cleaned_data['task']

            # todos.append(task)
            request.session['todos'].append(task)
            return HttpResponseRedirect(reverse('todolist:index'))
        else:
            return render(request, 'todolist/add_todo.html', {
                'form': form
            })


        #Manual Form Submission
        # todo = request.POST['todo']
        # todos.append(todo)

def clear_todos(request):
    request.session['todos'] = []
    request.session.modified = True
    return HttpResponseRedirect(reverse('todolist:index'))

def remove_todo(request, index):
    request.session['todos'].pop(index)
    request.session.modified = True
    return HttpResponseRedirect(reverse('todolist:index'))