from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms


class NewTodoForm(forms.Form):
    task = forms.CharField(label='Todo ')
    # priority = forms.IntegerField(min_value=0, max_value=3)


# todos = ['wash the cat', 'water the plants', 'walk the dog', 'ride the llama']

# Create your views here.
def todo(request):

    if 'todos' not in request.session:
        request.session['todos'] = []

    return render(request, 'todo_list/index.html', {
        # 'todos': todos
        'todos': request.session['todos']
    })


def add_todo(request):
    if request.method == 'GET':
        return render(request, 'todo_list/add_todo.html', {
            'form': NewTodoForm()
        })
    elif request.method == 'POST':

        form = NewTodoForm(request.POST)

        if form.is_valid():
            request.session.modified = True
            task = form.cleaned_data['task']

            # todos.append(task)
            request.session['todos'].append(task)
        else:
            return render(request, 'todo_list/add_todo.html', {
                'form': form
            })

        # Manual form submission
        # todo = (request.POST['todo'])
        # todos.append(todo)
        return HttpResponseRedirect(reverse('todo_list:index'))
