from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.all_books, name='store'),
    url(r'^book/(?P<book_id>[0-9]+)$', views.book_by_id, name='book_by_id'),
    url(r'^book/(?P<book_id>[0-9]+)/edit_book/$', views.edit_book, name='edit_book'),
    url(r'^book/(?P<pk>[0-9]+)/delete_book/$', views.DeleteBook.as_view(), name='book_delete'),
    url(r'^add_book/$', views.add_book, name='add_book'),
    url(r'^add_genre/$', views.add_genre, name='add_genre'),
    url(r'^add_author/$', views.add_author, name='add_author'),
    url(r'^genre/(?P<genre_id>[0-9]+)$', views.books_by_genre, name='books_by_genre'),
    url(r'^genre/(?P<genre_id>[0-9]+)/edit_genre/$', views.edit_genre, name='edit_genre'),
    url(r'^author/(?P<author_id>[0-9]+)$', views.books_by_author, name='books_by_author'),
    url(r'^author/(?P<author_id>[0-9]+)/edit_author/$', views.edit_author, name='edit_author'),
    url(r'^book/(?P<book_id>[0-9]+)/add_book_to_favorites/$', views.add_book_to_favorites, name='add_to_favorites'),
    url(r'^book/(?P<book_id>[0-9]+)/remove_book_from_favorites/$', views.remove_book_from_favorites, name='remove_from_favorites'),
]
