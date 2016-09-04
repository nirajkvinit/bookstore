from django.shortcuts import render
# from django.http import HttpResponse

from .models import Book


def index(request):
    latest_books_list = Book.objects.order_by('-approve_date')[:10]
    context = {'latest_books_list': latest_books_list}
    return render(request, 'store/index.html', context)
# Create your views here.
