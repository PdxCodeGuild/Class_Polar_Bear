from django.shortcuts import render
from .models import Book, Status


# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, 'library/index.html', {
        'books': books,
    })

# def checkin(request):
#     if



# Contributors: Ryan Gaston, Mark Wilson, Bowie Hall, Ken Mazur, Irron, Gabe Chacon