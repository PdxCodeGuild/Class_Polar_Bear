from django.shortcuts import render

todos =['test yourlife', 'mortal kombat']

# Create your views here.
def todo(request):
    return render(request, 'todolist/index.html',{

    'todos':todos
    })

def addtodo(request):
    return render(request,'todolist/add_todolist.html')


#  <!-- <a href ="{% url 'todolist:dd_todo' %}">Home</a> -->