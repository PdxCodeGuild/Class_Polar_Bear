from django.shortcuts import render
from .forms import NewRegistrationForm, NewLoginForm, NewPostForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import BlogPost

# Create your views here.
def home(request):
    blogs = BlogPost.objects.all().order_by('-date_created')[:10]
    return render(request, 'blog/index.html', {
        'blogs':blogs,
    })


def register(request):
    # will get the user to the registration page
    if request.method == 'GET':
        form = NewRegistrationForm()
        return render(request, 'blog/register.html', {
            'form':form,
            })

    # will allow the user to register and send them back to the
    # login page
    elif request.method == 'POST':
        form = NewRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
            )
            

            return HttpResponseRedirect(reverse('user_login'))


def user_login(request):
    if request.method == 'GET':
        form = NewLoginForm()
        return render(request, 'blog/user_login.html', {
            'form':form,
        })

    elif request.method == 'POST':
        form = NewLoginForm(request.POST)
        if form.is_valid():
            # authenticate method returns user or None
            user = authenticate(request, 
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
            )

            if user != None:
                login(request, user)
                return HttpResponseRedirect(reverse('profile'))
            
            else:
                form.add_error('username', 'Invalid username or password')
                return render(request, 'blog/user_login.html', {
                    'form':form
                })

@login_required(login_url='user_login')
def profile(request):
    blogs = BlogPost.objects.all().filter(user=request.user).order_by('-date_created')[:10]
    # title = blogs.title
    return render(request, 'blog/profile.html', {
        'blogs':blogs
    })

@login_required(login_url='user_login')
def create(request):
    if request.method == 'GET':
        form = NewPostForm()
        return render(request, 'blog/create.html', {
            'form':form,
        })
    
    elif request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            blog = BlogPost()
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.public = form.cleaned_data['user_choice']
            blog.user = request.user 
   
            
            blog.save()

            return HttpResponseRedirect(reverse('profile'))

@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required(login_url='user_login')
def blog_edit(request, blogpost_id):
    if request.method == 'GET':
        form = NewPostForm()
        blog = BlogPost.objects.get(id=blogpost_id)
        return render(request, 'blog/blog_edit.html', {
            'blog':blog,
            'form':form,
        })

    elif request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            blog = BlogPost.objects.get(id=blogpost_id)
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.public = form.cleaned_data['user_choice']

            blog.save()

            return HttpResponseRedirect(reverse('profile'))
        

@login_required(login_url='user_login')
def details(request, blogpost_id):
    blog = BlogPost.objects.get(id=blogpost_id)
    return render(request, 'blog/details.html', {
        'blog':blog,
    })