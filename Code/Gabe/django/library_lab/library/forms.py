from .utils import book_choices
from django import forms


class AvailableBookForm(forms.Form):
    user = forms.CharField(label='User', max_length=40)
    book = forms.ChoiceField(label='Book', choices=book_choices())
