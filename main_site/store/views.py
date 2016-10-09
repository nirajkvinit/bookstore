from django.shortcuts import render_to_response, redirect
from .models import Book, Genre, Author
from django.contrib import auth
from .forms import BookForm, GenreForm, AuthorForm
from django.core.context_processors import csrf


def index(request):
    latest_books_list = Book.objects.order_by('-approve_date')[:10]
    return render_to_response('store/index.html',
                              {'books': latest_books_list,
                               'username': auth.get_user(request).username})


def book_by_id(request, book_id):
    current_book = Book.objects.get(id=book_id)
    return render_to_response('store/book.html',
                              {'book': current_book,
                               'username': auth.get_user(request).username,
                               'votes_variants': range(1, 6)
                               }
                              )


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


def add_book(request):
    params = {}
    params.update(csrf(request))
    params['form'] = BookForm()
    if request.POST:
        newbook_form = BookForm(request.POST)
        if newbook_form.is_valid():
            newbook_form.save()
            return redirect('/')
        else:
            params['form'] = newbook_form
    return render_to_response('store/add_book.html', params)


def add_genre(request):
    params = {}
    params.update(csrf(request))
    params['form'] = GenreForm
    if request.POST:
        newgenre_form = GenreForm(request.POST)
        if newgenre_form.is_valid():
            newgenre_form.save()
            return redirect('/')
        else:
            params['form'] = newgenre_form
    return render_to_response('store/add_genre.html', params)


def add_author(request):
    params = {}
    params.update(csrf(request))
    params['form'] = AuthorForm
    if request.POST:
        newauthor_form = AuthorForm(request.POST)
        if newauthor_form.is_valid():
            newauthor_form.save()
            return redirect('/')
        else:
            params['form'] = newauthor_form
    return render_to_response('store/add_author.html', params)


def add_vote(request, book_id, vote):
    try:
        current_book = Book.objects.get(id=book_id)
        current_book.upd_rating(int(vote))
        return redirect("/store/book/" + book_id + "")
    except:
        return redirect('oops/')
