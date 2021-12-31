from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from .models import Message
from django.urls import reverse
from django.utils import timezone
# Create your views here.

class NewMessageForm(forms.Form):
    text_content = forms.CharField(label='Message')
    user = forms.CharField(label="Name")

def home(request):
    messages = Message.objects.all().order_by('date')
    return render(request, 'board/index.html',{
        'messages': messages,
        'form' : NewMessageForm()
    })

def new_message(request):
    if request.method == 'POST':
        form = NewMessageForm(request.POST)
        if form.is_valid():
            form_text_content = form.cleaned_data['text_content']
            form_user = form.cleaned_data['user']

            message = Message()
            message.text_content = form_text_content
            message.user = form_user
            message.date = timezone.now()

            message.save()
    return HttpResponseRedirect(reverse('home'))
