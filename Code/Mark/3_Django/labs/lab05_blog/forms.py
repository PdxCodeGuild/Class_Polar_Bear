from django import forms

class NewPostForm(forms.Form):
    body = forms.CharField(label='Post', max_length=4000)

