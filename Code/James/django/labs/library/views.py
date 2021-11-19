from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from .models import Author, Book, Track

# Create your views here.

def checkin(request):
    return render(request, "library/index.html")

def checkout(request, book_id):
    checked_book = Book.objects.get(id=book_id)
    track = Track()
    track.book = checked_book
    track.user = 'test5'
    track.checkout = True
    track.save()
    books = Book.objects.all().order_by("title")
    return render(request, "library/checkout.html", {
        "books": books,
    })




    

