from .models import Book

def book_choices():
    books = Book.objects.all()
    list_of_books = []
    for book in books:
        list_of_books.append((book.id, book.title))

    return list_of_books