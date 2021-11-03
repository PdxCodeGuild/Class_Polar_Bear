from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from board import models
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import Message


class NewMessageForm(forms.Form):
    text_content = forms.CharField(label='Message', max_length=240)
    user = forms.CharField(label='User', max_length=40)

# Create your views here.


def home_page(request):
    messages = Message.objects.all().order_by('-date')  # -date === inverse date

    return render(request, 'board/index.html', {
        'messages': messages,
        'form': NewMessageForm()
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
    return HttpResponseRedirect(reverse('message_board:home_page'))
