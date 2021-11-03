from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms

class NewTodoForm(forms.Form):
    task = forms.CharField(label="Todo")
    # priority = forms.IntegerField(min_value=0, max_value=5)


# todos = ['wash the cat', 'water the bird', 'walk the dog']


# request.session = {
#  'todos': []
# }



# Create your views here.
def todo(request):

    if "todos" not in request.session:
        request.session["todos"] = []

    print('index page:', request.session['todos'])
    return render(request, 'todolist/index.html', {
        # 'todos': todos
        'todos': request.session['todos']
    })

def add_todo(request):
    if request.method == "GET":
        return render(request, 'todolist/add_todo.html', {
            'form': NewTodoForm()
        })
    elif request.method == "POST":

        form = NewTodoForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data['task']

            # todos.append(task)
            request.session['todos'].append(task)

            # Notify django, session has updated
            request.session.modified = True
            print('Added todo', request.session['todos'])
            
            return HttpResponseRedirect(reverse('todolist:index'))
        else:
            return render(request, 'todolist/add_todo.html', {
                'form': form
            })
        # Manual form submission
        # todo = request.POST['todo']
        # todos.append(todo)

def remove_todo(request, index):
    request.session['todos'].pop(index)
    request.session.modified = True

    return HttpResponseRedirect(reverse('todolist:index'))

def clear_todos(request):
    request.session['todos'] = []
    request.session.modified = True

    return HttpResponseRedirect(reverse('todolist:index'))


# request.session = {
#   'todos': [
#       'walk the dog',
#       'feed the cat',
#       'water the grass'
#   ]
# }