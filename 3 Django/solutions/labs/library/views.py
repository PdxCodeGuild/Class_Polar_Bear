from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Book
from .forms import NewBookForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'library/index.html', {
        'books': books,
        'form': NewBookForm()
    })

def checkout(request):
    if request.method == "POST":
        form = NewBookForm(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data['book']
            book = Book.objects.get(id=book_id)
            book.state.checked_out = True
            book.state.user = form.cleaned_data['user']
            book.state.save()

    return HttpResponseRedirect(reverse('index'))