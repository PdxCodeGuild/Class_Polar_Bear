from django.shortcuts import render
# from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
#to use the models
from django.contrib.auth.models import User
#we import authenticate and capture login 
from django.contrib.auth import authenticate,login,logout

#we are importing this from the forms.py we created
from .forms import NewLoginForm,NewRegisterForm

  
# Create your views here.
def register(request):
    #if you are visiting the page show the user the form
    if request.method =="GET":
        form = NewRegisterForm()
        return render(request,'user_system/register.html',{
        'form':form
    })
    elif request.method =="POST":
        #django models already existing in django
        form = NewRegisterForm(request.POST)
        if form.is_valid():
            #create new user
            #coming from the user imported and create new user
            #we change to this because we have our own custom model
            # user=User()
            user =User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
                
            )

            #Assigning user attributes
            # user.username=form.cleaned_data['username']
            # user.first_name=form.cleaned_data['first_name']
            # user.last_name=form.cleaned_data['last_name']
            # user.email=form.cleaned_data['email']
            # user.password=form.cleaned_data['password']
            # user.save()

             

            #different
            # username = form.cleaned_data['username']
            # user.username =username

            return HttpResponseRedirect(reverse('login'))

def user_login(request):
    if request.method =='GET':
        return render(request, 'user_system/login.html',{
            'form': NewLoginForm()
        })
        #add something from django
    elif request.method == "POST":
        #grab the form
        form = NewLoginForm(request.POST)
        if form.is_valid():
            #this one can be put in as a whole
            password =form.cleaned_data['password']
            #from djano contrib, auth
            #returns user or none 
            user=authenticate(request, username=form.cleaned_data['username'],password =password)
            if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('profile'))
            else:
                #add error capture
                form.add_error('username','Invalid credentials')
                return render(request,'user_system/login.html',{
                    'form':form
                })
def profile(request):
    return render(request,'user_system/profile.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
