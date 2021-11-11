from django.shortcuts import render, get_object_or_404
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import BlogPost


class NewRegistryForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name', max_length=20)
    last_name = forms.CharField(label='Last Name', max_length=20)
    email = forms.EmailField(label='Email')


class NewLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class NewPost(forms.Form):
    title = forms.CharField(label='Title', max_length=40)
    body = forms.CharField(label='Body', max_length=1000)


# Create your views here.


def register(request):
    if request.method == 'GET':
        form = NewRegistryForm()
        return render(request, 'blog/register.html', {
            'form': form
        })
    elif request.method == 'POST':
        form = NewRegistryForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
            )
    return HttpResponseRedirect(reverse('blog:login'))


def user_login(request):
    if request.method == 'GET':
        form = NewLoginForm()
        return render(request, 'blog/login.html', {
            'form': form
        })
    elif request.method == 'POST':
        form = NewLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(
                    reverse('blog:profile')
                )
            else:
                form.add_error('username', 'Username or password incorrect')
                return render(request, 'blog/login.html', {
                    'form': form
                })


def profile(request):
    blogs = BlogPost.objects.filter(user=request.user)
    return render(request, 'blog/profile.html', {
        'blogs': blogs
    })


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:login'))


def create_post(request):
    if request.method == 'GET':
        form = NewPost()
        return render(request, 'blog/create.html', {
            'form': form
        })
    elif request.method == 'POST':
        form = NewPost(request.POST)
        if form.is_valid():
            create = BlogPost.objects.create_user(
                title=form.cleaned_data['title'],
                body=form.cleaned_data['body'],
                username=request.user
            )
        return HttpResponseRedirect(reverse('blog:profile'))
