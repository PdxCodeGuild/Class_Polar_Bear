from django import forms

class NewPostForm(forms.Form):
    text = forms.CharField(label='Post', max_length=120)

