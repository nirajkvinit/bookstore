from django.contrib import admin
from store.models import Author, Book, Genre

class AuthorAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    fields = ['name', 'pub_date', 'genre', 'author']


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)

