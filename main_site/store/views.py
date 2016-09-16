# from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Book


def index(request):
    latest_books_list = Book.objects.order_by('-approve_date')
    template = loader.get_template('store/index.html')
    context = RequestContext(request, {'books': latest_books_list})
    return HttpResponse(template.render(context))
