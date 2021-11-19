from django.shortcuts import render

from .models import Book
from .forms import NewBookForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'library/index.html', {
        'books': books,
        'form': NewBookForm()
    })