from django import forms
from django.forms.widgets import PasswordInput, Textarea
from .models import BlogPost

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=15)
    email = forms.EmailField()
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)

class NewBlogPost(forms.Form):
    title = forms.CharField(max_length=25)
    body = forms.CharField(widget=forms.Textarea)