from django import forms

class ToggleItemForm(forms.Form):
    completed = forms.CharField(widget=forms.CheckboxInput())