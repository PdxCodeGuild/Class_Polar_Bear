from django.forms.widgets import PasswordInput
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


from .forms import NewUserForm, UserLoginForm


def register(request):
    if request.method == 'POST':
        registration_form = NewUserForm(request.POST)
        if registration_form.is_valid():
            username = registration_form.cleaned_data['username']
            pasword = registration_form.cleaned_data['password']
            first_name = registration_form.cleaned_data['first_name']
            last_name = registration_form.cleaned_data['last_name']
            email = registration_form.cleaned_data['email']

            user = User.objects.create_user(
                username=username,
                password=pasword,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            user.save()
            print(user)
            return render(request, 'profile.html')
    else:
        form = NewUserForm()
        return render(request, 'register.html', {
            'form': NewUserForm
        })


def user_login(request):
    if request.method == 'GET':
        login_form = UserLoginForm()
        return render(request, 'login.html', {
            'form': login_form
        })
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return render(request, 'profile.html')
        else:
            return HttpResponse("Not cool")


@login_required(login_url='users/user_login')
def welcome(request):
    return render(request, 'welcome.html')
