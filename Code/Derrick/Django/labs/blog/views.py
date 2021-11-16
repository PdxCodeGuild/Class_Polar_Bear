from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import EditBlogPost, LoginForm, RegisterForm, NewBlogPost
from .models import BlogPost


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
            
        return HttpResponseRedirect(reverse('blog:login'))

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
def profile(request):
    posts = BlogPost.objects.all().filter(user=request.user)
    return render(request,'blog/profile.html',{'posts': posts})
    
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

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:login'))

@login_required
def edit(request,post_id):
    posts = BlogPost.objects.all().filter(id=post_id, user=request.user)
    post = posts.get(id=post_id)
    
    if request.method == 'POST':
        form = EditBlogPost(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return HttpResponseRedirect(reverse('blog:profile'))
    else:
        form = EditBlogPost({'title':post.title,'body':post.body}) # allows user to edit original post inside of the form
        return render(request,'blog/edit.html',{'form': form,'post': post, 'posts': posts})

@login_required
def posts(request):
    posts = BlogPost.objects.all()
    return render(request,'blog/posts.html',{'posts': posts})

@login_required
def details(request,post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request,'blog/details.html',{'post': post})

