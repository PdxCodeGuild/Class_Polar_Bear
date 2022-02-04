from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserLogin, UserSignup
from django.contrib.auth.decorators import login_required
from posts.models import BlogPost

# Create your views here.
def register(request):
    if request.method =="GET":
        form = UserSignup()
        args = {
            'form':form
        }
        return render(request, 'users/register.html', args)
    elif request.method == "POST":
        form = UserSignup(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                password=form.cleaned_data['password'],
                username = form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
            )
            return HttpResponseRedirect('login')

def login_user(request):
    if request.method == "GET":
        # form = UserLogin()
        args = {
            'form':UserLogin()
        }
        return render(request, 'users/login.html', args)
    elif request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = authenticate(request,username=form.cleaned_data['username'],password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('profile'))
            else:
                form.add_error('Incorrect login info')
                return render(request, 'login', {
                        'form': form
                    })

@login_required
def profile(request):
    args = ''
    return render(request, 'users/profile.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def profile(request):
    if not request.user.is_anonymous: 
        blog_list = BlogPost.objects.filter(user=request.user)
        args = {
            'blog_list': blog_list
        }
        print(blog_list, 'blog list')
        return render(request, 'users/profile.html', args)
    else:
        print('failure to login')