from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Message

# Create your views here.

class NewMessage(forms.Form):
    text = forms.CharField(label='Message: ',max_length=240)
    user = forms.CharField(label='Username: ',max_length=40)

def render_board(request):
    messages = Message.objects.all().order_by('-date')
    return render(request,'board/board.html',{
        'form': NewMessage(),
        'messages':messages,
    })

def send_message(request):
    if request.method == 'POST':
        form = NewMessage(request.POST)
        if form.is_valid():
            form_text = form.cleaned_data['text']
            form_user = form.cleaned_data['user']
            message = Message()
            message.text = form_text 
            message.user = form_user
            message.save()

    return HttpResponseRedirect(reverse('message_board'))
    