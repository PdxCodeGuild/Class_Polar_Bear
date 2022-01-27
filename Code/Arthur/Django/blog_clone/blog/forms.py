from django import forms

class newBlogForm(forms.Form):
    text = forms.CharField(label='blog', max_length=120)
