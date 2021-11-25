from django import forms

class NewBlurbForm(forms.Form):
    text = forms.CharField(label='Blurb', max_length=500)

class NewReplyForm(forms.Form):
    text = forms.CharField(label='Reply', max_length=500)