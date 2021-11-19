from django import forms

class NewSignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name', max_length=20)
    last_name = forms.CharField(label='Last Name', max_length=20)
    email = forms.EmailField(label='Email')


class NewLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput, max_length=10)