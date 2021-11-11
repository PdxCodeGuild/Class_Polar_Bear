from django import forms


class NewUserForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=20)
    last_name = forms.CharField(label='Last name', max_length=20)
    username = forms.CharField(label='Username', max_length=20)
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput(), max_length=18)


class UserLoginForm (forms.Form):
    username = forms.CharField(label="Username", max_length=20)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=18)
