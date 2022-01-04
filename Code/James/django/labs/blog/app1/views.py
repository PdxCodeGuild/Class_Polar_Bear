from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import BlogPost, UserAndPassword
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



# Create your views here.

def profile(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'app1/profile.html', context)

def create(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'app1/create.html', context)

def mycreate(request):
    # print(request.POST)
    # return HttpResponse('form received')
    title = request.POST['title']
    body = request.POST['body']
    user = request.user # Capitalize?
    blogpost = BlogPost(title=title, body=body, user=user)
    blogpost.save()
    return HttpResponseRedirect(reverse('app1:profile')) 

'''def myusercreate(request):
    username = request.POST['username']     
    password = request.POST['password']
    userandpassword = UserAndPassword(password=password, username=username)
    userandpassword.save()
    return HttpResponseRedirect(reverse('app1:register'))'''

def register(request):
    # retrieve the variables from the form submission
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'app1/profile.html')
    # else:
        # return an 'invalid login' error message

def mylogin(request):
    # retrieve the variables from the form submission
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'app1/profile.html')
    # else:
        # return an 'invalid login' error message
