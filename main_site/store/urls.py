from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.all_books),
    url(r'^book/(?P<book_id>[0-9]+)$', views.book_by_id),
    url(r'^genre/(?P<genre_id>[0-9]+)$', views.books_by_genre),
    url(r'^author/(?P<author_id>[0-9]+)$', views.books_by_author),
]
