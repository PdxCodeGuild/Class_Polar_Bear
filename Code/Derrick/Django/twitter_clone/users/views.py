from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NewLoginForm, NewSignupForm

# Create your views here.
def signup(request):
    if request.method == "GET":
        form = NewSignupForm()
        return render(request, 'users/signup.html', {
            'form': form
        })
    elif request.method == "POST":
        form = NewSignupForm(request.POST)
        if form.is_valid():

            user = User.objects.create_user(
                username= form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            return HttpResponseRedirect(reverse('login'))


def user_login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html', {
            'form': NewLoginForm()
        })

    elif request.method == "POST":
        form = NewLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password) # returns a user or None
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('profile'))
            else:
                return render(request, 'users/login.html', {
                    'form': form
                })

def profile(request):
    return render(request, 'users/profile.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))