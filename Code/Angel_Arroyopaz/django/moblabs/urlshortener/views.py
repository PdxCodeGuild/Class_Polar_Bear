from django import shortcuts
from django.db.models.fields import CharField
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from .models import ShortenedURL
import string
import random

lowercase_letters = string.ascii_letters
uppercase_letters = string.ascii_uppercase
numbers = string.digits

class Urlform(forms.Form):
    user_input = forms.CharField(label='url', max_length=100)


# Create your views here.
def shortener(request):
    short_urls = ShortenedURL.objects.all().order_by('id')
    return render(request, 'urlshortener/index.html', {
        'form':Urlform(),
        'short_urls':short_urls
    })

def save_url(request):
    if request.method == 'POST':
        form = Urlform(request.POST)
        if form.is_valid():
            form_url = form.cleaned_data['user_input']
            shortenedurl = ShortenedURL()
            shortenedurl.url = form_url
            shortenedurl.code = urlgenerator()
            shortenedurl.counter += 1
            shortenedurl.save()

    return HttpResponseRedirect(reverse('shortener'))


def urlgenerator():
    shortversion = ""

    for i in range(6):
        shortversion += random.choice(string.ascii_letters)

    return shortversion

def url_redirect(request, code):
    redirected_url = ShortenedURL.objects.get(code = code)

    return HttpResponseRedirect(redirected_url.url)



