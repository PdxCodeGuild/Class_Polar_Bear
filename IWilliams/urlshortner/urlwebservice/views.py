from django.shortcuts import render
from django import forms
from .models import ShortenedURL
from django.http import HttpResponseRedirect
from django.urls import reverse

import random
import string

# Create your views here.
class URLform(forms.Form): 
    user_input = forms.CharField(label='Enter url')


def index(request):
    shorturls = ShortenedURL.objects.all().order_by('id')
    return render(request, 'urlshortner/index.html', {
        'form' : URLform(),
        'shorturls' : shorturls 
        
        })

def saveurl(request):
    if request.method == 'POST': 
        form = URLform(request.POST)
        if form.is_valid(): 
            form_url = form.cleaned_data['user_input']
            shortenedurl2 = ShortenedURL()
            shortenedurl2.url = form_url
            # shortenedurl2.url = urlgenerator(form_url)
            shortenedurl2.code = urlgenerator()
            shortenedurl2.save()

    return HttpResponseRedirect(reverse('index'))


def urlgenerator():
    shortname = ''
    for i in range(6): 
        shortname += random.choice(string.ascii_letters)
    
    # uppercase = string.ascii_letters.upper()
    # shortname = random.choice(uppercase) 
     
    return shortname


def urlredirect(request, code): 
    redirecturl = ShortenedURL.objects.get(code = code)
    redirecturl.counter +=1

    redirecturl.save()
    return HttpResponseRedirect(redirecturl.url)
