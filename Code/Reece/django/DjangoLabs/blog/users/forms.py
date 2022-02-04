from django import forms

class UserSignup(forms.Form):
    username = forms.CharField(label='Username',max_length=25)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=25)
    first_name = forms.CharField(label='First Name', max_length=15)
    last_name = forms.CharField(label='Last Name', max_length=15)
    email = forms.EmailField(label='Email')

class UserLogin(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=10)