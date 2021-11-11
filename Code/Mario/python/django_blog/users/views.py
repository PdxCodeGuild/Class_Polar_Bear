from django.forms.widgets import PasswordInput
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

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
            return HttpResponse('cool')
    else:
        form = NewUserForm()
        return render(request, 'register.html', {
            'form': NewUserForm
        })


def login(request):
    login_form = UserLoginForm()
    return render(request, 'login.html', {
        'form': login_form
    })
