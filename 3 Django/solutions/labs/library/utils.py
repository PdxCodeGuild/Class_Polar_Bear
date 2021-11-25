from .models import Book

def book_choices(checked_out=False):
    books = Book.objects.all().filter(state__checked_out=checked_out)
    # print(books)
    list_of_books = []
    for book in books:
        list_of_books.append((book.id, book.title))

    return list_of_books