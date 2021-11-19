from django.shortcuts import render
from .models import Book, Status


# Create your views here.


def index(request):
    return render(request, 'library/index.html')


# Contributors: Ryan Gaston, Mark Wilson, Bowie Hall, Ken Mazur, Irron, Gabe Chacon
