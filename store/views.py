from django.shortcuts import redirect, render
from .models import Book, Genre, Author
from django.contrib import auth
from .forms import BookForm, GenreForm, AuthorForm
from django.core.context_processors import csrf
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


def index(request):
    params = {}
    params['books'] = Book.objects.order_by('-approve_date')[:10]
    params['authors'] = Author.objects.all()
    params['genres'] = Genre.objects.all()
    return render(request, template_name='store/index.html', context=params)


def book_by_id(request, book_id):
    params = {}
    params['book'] = Book.objects.select_related().get(id=book_id)
    params['votes_variants'] = range(1, 6)
    return render(request, template_name='store/book.html', context=params)


def books_by_genre(request, genre_id):
    params = {}
    params['genre'] = Genre.objects.get(id=genre_id)
    params['books'] = Book.objects.filter(genre=genre_id)
    return render(request, template_name='store/genre.html', context=params)


def books_by_author(request, author_id):
    params = {}
    params['author'] = Author.objects.get(id=author_id)
    params['books'] = Book.objects.filter(author=author_id)
    return render(request, template_name='store/author.html', context=params)


def all_books(request):
    params = {}
    params['books'] = Book.objects.order_by('-approve_date')
    params['username'] = auth.get_user(request).username
    # реализовать пагинацию // realize pagination через CBV
    return render(request, template_name='store/store.html', context=params)


@login_required
def add_book(request):
    params = {}
    params.update(csrf(request))
    params['form'] = BookForm()
    params['action'] = "/store/add_book/"
    params['button_value'] = "Create Book"
    if request.POST:
        newbook_form = BookForm(request.POST)
        if newbook_form.is_valid():
            newbook_form.save()
            return redirect('/')
        else:
            params['form'] = newbook_form
    return render(request,
                  template_name='store/add_edit_form.html',
                  context=params)


@login_required
def add_genre(request):
    params = {}
    params.update(csrf(request))
    params['form'] = GenreForm
    params['action'] = "/store/add_genre/"
    params['button_value'] = "Create Genre"
    if request.POST:
        newgenre_form = GenreForm(request.POST)
        if newgenre_form.is_valid():
            newgenre_form.save()
            return redirect('/')
        else:
            params['form'] = newgenre_form
    return render(request,
                  template_name='store/add_edit_form.html',
                  context=params)


@login_required
def add_author(request):
    params = {}
    params.update(csrf(request))
    params['form'] = AuthorForm
    params['action'] = "/store/add_author/"
    params['button_value'] = "Create Author"
    if request.POST:
        newauthor_form = AuthorForm(request.POST)
        if newauthor_form.is_valid():
            newauthor_form.save()
            return redirect('/')
        else:
            params['form'] = newauthor_form
    return render(request,
                  template_name='store/add_edit_form.html',
                  context=params)


@login_required
def edit_book(request, book_id):
    params = {}
    params.update(csrf(request))
    params['book'] = Book.objects.get(id=book_id)
    params['form'] = BookForm(instance=params['book'])
    params['action'] = "/store/book/" + book_id + "/edit_book/"
    params['button_value'] = "Update Book"
    if request.POST:
        editbook_form = BookForm(request.POST, instance=params['book'])
        if editbook_form.is_valid():
            editbook_form.save()
            return redirect("/store/book/" + book_id + "")
        else:
            params['form'] = editbook_form
    else:
        return render(request,
                      template_name='store/add_edit_form.html',
                      context=params)


@login_required
def edit_author(request, author_id):
    params = {}
    params.update(csrf(request))
    params['author'] = Author.objects.get(id=author_id)
    params['form'] = AuthorForm(instance=params['author'])
    params['action'] = "/store/author/" + author_id + "/edit_author/"
    params['button_value'] = "Update Author"
    if request.POST:
        editauthor_form = AuthorForm(request.POST, instance=params['author'])
        if editauthor_form.is_valid():
            editauthor_form.save()
            return redirect("/store/author/" + author_id + "")
        else:
            params['form'] = editauthor_form
    else:
        return render(request,
                      template_name='store/add_edit_form.html',
                      context=params)


@login_required
def edit_genre(request, genre_id):
    params = {}
    params.update(csrf(request))
    params['genre'] = Genre.objects.get(id=genre_id)
    params['form'] = GenreForm(instance=params['genre'])
    params['action'] = "/store/genre/" + genre_id + "/edit_genre/"
    params['button_value'] = "Update Genre"
    if request.POST:
        editgenre_form = GenreForm(request.POST, instance=params['genre'])
        if editgenre_form.is_valid():
            editgenre_form.save()
            return redirect("/store/genre/" + genre_id + "")
        else:
            params['form'] = editgenre_form
    else:
        return render(request,
                      template_name='store/add_edit_form.html',
                      context=params)


@login_required
def add_book_to_favorites(request, book_id):
    current_book = Book.objects.get(id=book_id)
    if request.user.is_authenticated():
        try:
            current_user = User.objects.get(id=auth.get_user(request).id)
            current_book.favorite_by.add(current_user.profile)
            current_book.save()
            print('its okay, book appllied to favorites')
            return redirect("/store/book/" + book_id + "")
        except:
            return redirect('/oops/')


class DeleteBook(DeleteView):
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteBook, self).dispatch(request, *args, **kwargs)
    model = Book
    template_name = 'store/book_del_conf.html'
    success_url = '/store/'
