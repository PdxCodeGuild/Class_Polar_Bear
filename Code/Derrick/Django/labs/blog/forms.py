from django import forms
from django.forms import ModelForm
from .models import BlogPost

# from .models import BlogPost
# from django.forms.widgets import PasswordInput, Textarea

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=15, widget=forms.widgets.TextInput(attrs={'placeholder':'Username'}))
    email = forms.CharField(widget=forms.widgets.EmailInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(max_length=15, widget=forms.widgets.PasswordInput(attrs={'placeholder':'Password'}))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=15, widget=forms.widgets.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(max_length=15, widget=forms.widgets.PasswordInput(attrs={'placeholder':'Password'}))

class NewBlogPost(forms.Form):
    title = forms.CharField(max_length=25)
    body = forms.CharField(widget=forms.widgets.Textarea)

class EditBlogPost(forms.Form):
    title = forms.CharField(max_length=25)
    body = forms.CharField(widget=forms.widgets.Textarea)



         