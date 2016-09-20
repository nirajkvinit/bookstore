from django.shortcuts import render_to_response
from .models import Book


def index(request):
    latest_books_list = Book.objects.order_by('-approve_date')
    return render_to_response('store/index.html', {'books': latest_books_list})
