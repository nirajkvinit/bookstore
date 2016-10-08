from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.all_books),
    url(r'^book/(?P<book_id>[0-9]+)$', views.book_by_id),
    url(r'^book/(?P<book_id>[0-9]+)/add_vote/(?P<vote>[0-9]+)$', views.add_vote),
    url(r'^add_book/$', views.add_book),
    url(r'^add_genre/$', views.add_genre),
    url(r'^add_author/$', views.add_author),
    url(r'^genre/(?P<genre_id>[0-9]+)$', views.books_by_genre),
    url(r'^author/(?P<author_id>[0-9]+)$', views.books_by_author),
]
