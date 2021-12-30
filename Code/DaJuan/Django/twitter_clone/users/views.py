from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

class NewSignupForm(forms.Form):
    username = forms.CharField(label= 'Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput,   label='Password', max_length=15)
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')

class NewLoginForm(forms.Form):
    username = forms.CharField(label= 'Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput,   label='Password', max_length=15)
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')

# Views

def signup(request):
    if request.method == 'GET':
        form = NewSignupForm()
        return render(request, 'users/signup.html', {
        'form' : form,
    })

    elif request.method == 'POST':
        form = NewSignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                first_name = form.cleaned_data['First Name'],
                last_name = form.cleaned_data['Last Name'],
                email = form.cleaned_data['Email'],
                password = form.cleaned_data['Password']
            )
        
        
        
        
         #   user.username = form.cleaned_data['username']
          #  user.first_name = form.cleaned_data['First Name']
           # user.last_name = form.cleaned_data['Last Name']
          #  user.email = form.cleaned_data['Email']
           # user.password = form.cleaned_data['Password']

            return HttpResponseRedirect(reverse('login'))

def user_login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html', {
            'form' : NewLoginForm()
        })

    elif request.method == 'POST':
        form = NewLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'])
            password = form.cleaned_data['password']
            if user is not None:
                login(request, user)
            else:
                form.add_error('username', 'invalid credentials')
                return render(request, 'users/login.html', {
                    'form' : form
                })