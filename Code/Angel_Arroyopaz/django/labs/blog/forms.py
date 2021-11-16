from django import forms
from django.forms.widgets import TextInput   

class NewRegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=25)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=25)
    first_name = forms.CharField(label='First Name', max_length=20)
    last_name = forms.CharField(label='Last Name', max_length=20)
    email = forms.EmailField(label='Email')

class NewLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=25)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=25)

class NewPostForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your blog\'s title goes here', 'cols':30, 'rows':3}), label='', max_length=100)
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your blog\'s body goes here'}), label='', max_length=1000)
    user_choice = forms.NullBooleanField(widget=forms.RadioSelect(choices=[(True, 'Public'), (False, 'Private')]))
   