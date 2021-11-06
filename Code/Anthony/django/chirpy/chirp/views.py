from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import Cheep
# Create your views here.


class NewCheepForm(forms.Form):
    text = forms.CharField(label='Cheep your thoughts here...', max_length=120)

def index(request):
    cheeps = Cheep.objects.filter(deleted=False).order_by('-date_published')
    return render(request, 'chirp/index.html', {
        'form': NewCheepForm(),
        'cheeps': cheeps
    })

def save_cheep(request):
    if request.method == "POST":
        form = NewCheepForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user = request.user

            cheep = Cheep()
            cheep.chirp = text
            cheep.user = user
            cheep.save()

    return HttpResponseRedirect(reverse('filter'))


def nono_filter(request):
    banned_words = ['llama', 'panda', 'Ilama', 'lIama', 'IIama']

    cheeps = Cheep.objects.filter(deleted=False)

    for cheep in cheeps:
        for nono in banned_words:
            if nono in cheep.chirp:
                cheep.deleted = True
                cheep.save()

    return HttpResponseRedirect(reverse('index'))