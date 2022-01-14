from django import forms

class NewRegisterForm(forms.Form):
    username =forms.CharField(label='Username', max_length=40)
    password = forms.CharField(widget =forms.PasswordInput,label='Password',max_length =20)
    first_name =forms.CharField(label='First Name', max_length=40)
    last_name =forms.CharField(label='Last Name', max_length=40)
    email =forms.EmailField(label='Email')

class NewLoginForm(forms.Form):
    username =forms.CharField(label='Username', max_length=40)
    password = forms.CharField(widget =forms.PasswordInput,label='Password',max_length =20)
  