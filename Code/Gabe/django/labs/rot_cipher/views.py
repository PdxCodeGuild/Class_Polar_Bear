from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms

# Logic


def find_word(word, amount=13):
    english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ''
    for letter in word:
        index = english.index(letter)

        if index + amount > len(english) - 1:
            remain = amount - (len(english) - index)
            result += english[remain % 26]
        else:
            result += english[index + amount]
    return result


class NewForm(forms.Form):
    word = forms.CharField(label='Word to cypher ')
    amount = forms.IntegerField(label='Amount of turns (optional: default 13)')


# Create your views here.
def rot_cipher(request):
    if 'word_to_cipher' not in request.session:
        request.session['word_to_cipher'] = []
    if 'ciphered' not in request.session:
        request.session['ciphered'] = []
    return render(request, 'rot_cipher/index.html', {
        'length': len(request.session['word_to_cipher']),
        'word_to_cipher': request.session['word_to_cipher'],
        'ciphered': request.session['ciphered']
    })


def cipher_word(request):
    if request.method == 'GET':
        return render(request, 'rot_cipher/cipher_word.html', {
            'form': NewForm()
        })
    elif request.method == 'POST':

        form = NewForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            amount = form.cleaned_data['amount']

            request.session['word_to_cipher'].append(word)
            request.session['ciphered'].append(find_word(word, amount))
            request.session.modified = True

            return HttpResponseRedirect(reverse('rot_cipher:index'))
        else:
            return render(request, 'rot_cypher/cipher_word.html', {
                'form': form
            })


def remove_word(request, index):
    request.session['word_to_cipher'].pop(index)
    request.session['ciphered'].pop(index)
    request.session.modified = True
    return HttpResponseRedirect(reverse('rot_cipher:index'))


def clear(request):
    request.session['word_to_cipher'].clear()
    request.session['ciphered'].clear()
    request.session.modified = True
    return HttpResponseRedirect(reverse('rot_cipher:index'))
