from django import forms
from .utils import book_choices



class NewBookForm(forms.Form):
    user = forms.CharField(label='Name', max_length=40)
    book = forms.ChoiceField(label='Book', choices=book_choices())