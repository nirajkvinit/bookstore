from django.forms import ModelForm, Form
from .models import Author, Genre, Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'pub_date', 'genre', 'author']


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'gender']
