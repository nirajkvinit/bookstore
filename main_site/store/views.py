from django.shortcuts import render_to_response, redirect
from .models import Book, Genre, Author
from django.contrib import auth
from .forms import BookForm, GenreForm, AuthorForm
from django.core.context_processors import csrf


def index(request):
    latest_books_list = Book.objects.order_by('-approve_date')[:10]
    all_authors = Author.objects.all()
    all_genres = Genre.objects.all()
    return render_to_response('store/index.html',
                              {'books': latest_books_list,
                               'authors': all_authors,
                               'genres': all_genres,
                               'username': auth.get_user(request).username})


def book_by_id(request, book_id):
    current_book = Book.objects.select_related().get(id=book_id)
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
                              {'books': books,
                               'username': auth.get_user(request).username,
                               'genre': current_genre})


def books_by_author(request, author_id):
    current_author = Author.objects.get(id=author_id)
    books = Book.objects.filter(author=author_id)
    return render_to_response('store/author.html',
                              {'books': books,
                               'username': auth.get_user(request).username,
                               'author': current_author})


def all_books(request):
    all_books = Book.objects.order_by('-approve_date')
    # реализовать пагинацию // realize pagination
    return render_to_response('store/store.html',
                              {'books': all_books,
                               'username': auth.get_user(request).username,
                               })


def add_book(request):
    params = {}
    params.update(csrf(request))
    params['form'] = BookForm()
    params['action'] = "/store/add_book/"
    params['button_value'] = "Create Book"
    params['username'] = auth.get_user(request).username
    if request.POST:
        newbook_form = BookForm(request.POST)
        if newbook_form.is_valid():
            newbook_form.save()
            return redirect('/')
        else:
            params['form'] = newbook_form
    return render_to_response('store/add_edit_form.html', params)


def add_genre(request):
    params = {}
    params.update(csrf(request))
    params['form'] = GenreForm
    params['action'] = "/store/add_genre/"
    params['button_value'] = "Create Genre"
    params['username'] = auth.get_user(request).username
    if request.POST:
        newgenre_form = GenreForm(request.POST)
        if newgenre_form.is_valid():
            newgenre_form.save()
            return redirect('/')
        else:
            params['form'] = newgenre_form
    return render_to_response('store/add_edit_form.html', params)


def add_author(request):
    params = {}
    params.update(csrf(request))
    params['form'] = AuthorForm
    params['action'] = "/store/add_author/"
    params['button_value'] = "Create Author"
    params['username'] = auth.get_user(request).username
    if request.POST:
        newauthor_form = AuthorForm(request.POST)
        if newauthor_form.is_valid():
            newauthor_form.save()
            return redirect('/')
        else:
            params['form'] = newauthor_form
    return render_to_response('store/add_edit_form.html', params)


def add_vote(request, book_id, vote):
    if request.user.is_authenticated():
        try:
            current_book = Book.objects.get(id=book_id)
            current_book.upd_rating(int(vote))
            return redirect("/store/book/" + book_id + "")
        except:
            return redirect('/oops/')
    else:
        return redirect('/login_required/')


def edit_book(request, book_id):
    params = {}
    params.update(csrf(request))
    params['book'] = Book.objects.get(id=book_id)
    params['form'] = BookForm(instance=params['book'])
    params['action'] = "/store/book/" + book_id + "/edit_book/"
    params['button_value'] = "Update Book"
    params['username'] = auth.get_user(request).username
    if request.POST:
        editbook_form = BookForm(request.POST, instance=params['book'])
        if editbook_form.is_valid():
            editbook_form.save()
            return redirect("/store/book/" + book_id + "")
        else:
            params['form'] = editbook_form
    else:
        return render_to_response('store/add_edit_form.html', params)
