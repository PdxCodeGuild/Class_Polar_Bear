from django import forms
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.utils import timezone

from .models import Message
# from current folder models import Message


class NewMessageForm(forms.Form):
    text_content = forms.CharField(label='Message', max_length=240)
    user = forms.CharField(label='user', max_length=40)

# Create your views here.
def home_page(request):
    messages = Message.objects.all().order_by('date') # grabs all the messages stored in message class /// the .order_by('date') order items by date. Can change it to '-date' for a reversed order
    return render(request, 'board/index.html', {
        'messages': messages,
        'form': NewMessageForm()
    })


# form submission function
def new_message(request):
    if request.method == "POST":
        form = NewMessageForm(request.POST)
        if form.is_valid():
            form_text_content = form.cleaned_data['text_content']
            form_user = form.cleaned_data['user']
            message = Message()
            message.text_content = form_text_content
            message.user = form_user
            message.date = timezone.now()

            message.save()

    return HttpResponseRedirect(reverse('home_page'))

