from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms

class AddTodoForm(forms.Form):
    task = forms.CharField(label="New Task")


# todos = ['task 1','task 2','task 3','task 4']

# Create your views here.

def todo(request):
    if 'todos' not in request.session:
        request.session['todos'] = []

    return render(request,'todo_list/index.html',{'todos': request.session['todos']})

def add(request):
    if request.method == 'GET':
        return render(request,'todo_list/add.html',{'form':AddTodoForm()})
    elif request.method == 'POST':
        form = AddTodoForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['todos'].append(task)
            request.session.modified = True
            return HttpResponseRedirect(reverse('todos'))
        else:
            return render(request,'add/add.html',{'form': form})
        # manual way
            # todos.append(request.POST['todo'])
            # return HttpResponseRedirect(reverse('todos'))