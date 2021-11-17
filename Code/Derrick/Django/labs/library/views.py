from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.urls import reverse
from .models import Book, Author
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request,'library/index.html',{'books': books})

def checkin_page(request):
    books = Book.objects.filter(checked_out=True)
    return render(request,'library/checkin.html',{'books': books})

def checkout_page(request):
    books = Book.objects.filter(checked_out=False)
    return render(request,'library/checkout.html',{'books': books})

def checkout_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.checked_out = True
    book.save()
    return HttpResponseRedirect(reverse('index'))

def checkin_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.checked_out = False
    book.save()
    return HttpResponseRedirect(reverse('index'))
    