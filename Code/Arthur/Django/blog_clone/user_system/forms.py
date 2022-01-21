from charset_normalizer import models
from django import forms

#we create our models using the classes
class NewRegisterForm(forms.Form):
    username =forms.CharField(label='Username', max_length=40)
    password = forms.CharField(widget =forms.PasswordInput,label='Password',max_length =20)
    first_name =forms.CharField(label='First Name', max_length=40)
    last_name =forms.CharField(label='Last Name', max_length=40)
    email =forms.EmailField(label='Email')
    date_created = models.DateTimeField(auto_now_add =True,null =True)

    def __str__(self):
        return str({self.username},{self.first_name},{self.last_name})

    

class NewLoginForm(forms.Form):
    username =forms.CharField(label='Username', max_length=40)
    password = forms.CharField(widget =forms.PasswordInput,label='Password',max_length =20)
  