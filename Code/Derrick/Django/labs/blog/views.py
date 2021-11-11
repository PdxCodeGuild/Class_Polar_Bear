from django.shortcuts import render
from .forms import LoginForm, RegisterForm, NewBlogPost
from .models import BlogPost
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        
        return render(request,'blog/register.html',{'form': form})

    elif request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password']
            )
            
        return render(request,'blog/profile.html')
@login_required
def profile(request):
    posts = BlogPost.objects.all().filter(user=request.user)
    return render(request,'blog/profile.html',{'posts': posts})

def user_login(request):
    if request.method == 'GET':
        return render(request,'blog/login.html',{'form': LoginForm()})

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user != None:
                login(request,user)

                return HttpResponseRedirect(reverse('blog:profile'))
            else:
                return render(request,'users/login.html')
    
@login_required
def create(request):
    if request.method == 'GET':
        return render(request,'blog/create.html',{'form':NewBlogPost()})

    elif request.method == 'POST':
        form = NewBlogPost(request.POST)

        if form.is_valid():
            post = BlogPost()
            post.user = request.user
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()

    return HttpResponseRedirect(reverse('blog:profile'))
            
    
        

