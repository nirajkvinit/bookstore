from django.shortcuts import render_to_response
from .models import Book, Genre, Author
from django.contrib import auth


def index(request):
    latest_books_list = Book.objects.order_by('-approve_date')[:10]
    return render_to_response('store/index.html',
                              {'books': latest_books_list,
                               'username': auth.get_user(request).username})


def book_by_id(request, book_id):
    current_book = Book.objects.get(id=book_id)
    return render_to_response('store/book.html',
                              {'book': current_book,
                               'username': auth.get_user(request).username})


def books_by_genre(request, genre_id):
    current_genre = Genre.objects.get(id=genre_id)
    books = Book.objects.filter(genre=genre_id)
    return render_to_response('store/genre.html',
                              {'books': books, 'genre': current_genre})


def books_by_author(request, author_id):
    current_author = Author.objects.get(id=author_id)
    books = Book.objects.filter(author=author_id)
    return render_to_response('store/author.html',
                              {'books': books, 'author': current_author})


def all_books(request):
    all_books = Book.objects.order_by('-approve_date')
    # реализовать пагинацию // realize pagination
    return render_to_response('store/index.html', {'books': all_books})
