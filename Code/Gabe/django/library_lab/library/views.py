from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Book, State
from .utils import book_choices


# class NewCheckOut(forms.Form):
#   title =
#   user =

# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, 'library/index.html', {
        'books': books
    })


def checkout(request):
    if request.method == 'POST':
        form = request.POST
        book_id = form['book']
        book = Book.objects.get(id=book_id)
        book.state.checked_out = True
        book.state.user = form['user']
        book.state.save()

    return HttpResponseRedirect(reverse('index'))


def checkin(request):
    if request.method == 'POST':
        form = request.POST
        book_id = form['book']
        book = Book.objects.get(id=book_id)
        book.state.checked_out = False
        book.state.save()
        return HttpResponseRedirect(reverse('index'))
    elif request.method == 'GET':
        books = Book.objects.all().filter(state__checked_out=True)
        return render(request, 'library/checkin.html', {
            'books': books
        })
