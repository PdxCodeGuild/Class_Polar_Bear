from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import ShortenedURL
from .utils import generate_code

class ShortenedURLForm(forms.Form):
    url = forms.URLField(label='Long URL')

# Create your views here.
def shortener(request):
    urls = ShortenedURL.objects.all().order_by('-counter')
    return render(request, 'url_shortener/shortener.html', {
        'form': ShortenedURLForm(),
        'urls': urls
    })

def save_url(request):
    if request.method == 'POST':
        form = ShortenedURLForm(request.POST)
        if form.is_valid():
            url = ShortenedURL()
            url.url = form.cleaned_data['url']
            url.code = generate_code()
            url.save()
    return HttpResponseRedirect(reverse('url_shortener:shortener'))

# localhost:8000/shortener/s58a6c
def redirect(request, code):
    url = ShortenedURL.objects.get(code=code)
    url.counter += 1
    url.save()
    return HttpResponseRedirect(url.url)