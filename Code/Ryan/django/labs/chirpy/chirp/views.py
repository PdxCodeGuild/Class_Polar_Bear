from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms 
from .models import Cheep
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
class NewCheepForm(forms.Form):
    text = forms.CharField(label='Cheep your thoughts here...', max_length=120)

    # who is currently signed in
    # request.user

def index(request):

    # cheeps = Cheep.objects.all().order_by('-date_published')
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
    # return HttpResponseRedirect(reverse('chirp:index'))
    return HttpResponseRedirect(reverse('filter'))
def nono_filter(request):
    banned_words = ['llama']
    cheeps = Cheep.objects.filter(deleted=False)

    for cheep in cheeps:
        for nono in banned_words:
            if nono in cheep.chirp:
                cheep.deleted = True
                cheep.save()
    # return HttpResponseRedirect(reverse('chirp:index'))
    return HttpResponseRedirect(reverse('index'))
