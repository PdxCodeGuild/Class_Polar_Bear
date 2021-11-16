from django import forms
from django.forms import ModelForm
from .models import BlogPost

# from .models import BlogPost
# from django.forms.widgets import PasswordInput, Textarea

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=15)
    email = forms.EmailField()
    password = forms.CharField(max_length=15, widget=forms.widgets.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=15, widget=forms.widgets.PasswordInput)

class NewBlogPost(forms.Form):
    title = forms.CharField(max_length=25)
    body = forms.CharField(widget=forms.widgets.Textarea)

class EditBlogPost(forms.Form):
    title = forms.CharField(max_length=25)
    body = forms.CharField(widget=forms.widgets.Textarea)



         