from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewSignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=10)
    first_name = forms.CharField(label='First Name', max_length=20)
    last_name = forms.CharField(label='Last Name', max_length=20)
    email = forms.EmailField(label='Email')

class NewLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=10)


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

            # Create new user
            user = User.objects.create_user(
                username= form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Assign user attributes
            # user.username = form.cleaned_data['username']
            # user.first_name = form.cleaned_data['first_name']
            # user.last_name = form.cleaned_data['last_name']
            # user.email = form.cleaned_data['email']
            # user.password = form.cleaned_data['password']
            # user.save()

            # Alternate version ----------------------
            # username = form.cleaned_data['username']
            # user.username = username

            return HttpResponseRedirect(reverse('login'))


def user_login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html', {
            'form': NewLoginForm()
        })

    elif request.method == "POST":
        form = NewLoginForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = authenticate(request,username=form.cleaned_data['username'],password=password) # returns a user or None
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('profile'))
            else:
                form.add_error('username', 'Invalid credentials')
                return render(request, 'users/login.html', {
                    'form': form
                })

def profile(request):
    return render(request, 'users/profile.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))