from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.urls import reverse
from .models import Book, Author
from .forms import UserForm
from datetime import datetime
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request,'library/index.html',{'books': books})

def checkin_page(request):
    books = Book.objects.filter(checked_out=True)
    form = UserForm()
    return render(request,'library/checkin.html',{'books': books,'form':form})

def checkout_page(request):
    books = Book.objects.filter(checked_out=False)
    form = UserForm()
    return render(request,'library/checkout.html',{'books': books,'form':form})

def checkout_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = UserForm(request.POST)
    if form.is_valid():
        book.name = form.cleaned_data['name']
        book.timestamp = datetime.now
    book.checked_out = True
    book.save()
    return HttpResponseRedirect(reverse('index'))

def checkin_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = UserForm(request.POST)
    if form.is_valid():
        book.name = form.cleaned_data['name']
        book.timestamp = datetime.now
    book.checked_out = False
    book.save()
    return HttpResponseRedirect(reverse('index'))

    