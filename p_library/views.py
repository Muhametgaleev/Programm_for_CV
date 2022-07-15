from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
from p_library.models import Book, Author


def books_list(request):
    books = Book.objects.all()
    for book in books:
        return HttpResponse(book.title)


def Author_list(request):
    authorss=''
    authors = Author.objects.all()
    # return HttpResponse(authors)
    for author in authors:
        authorss=authorss+author.full_name+" "
    return HttpResponse(authorss)

def index(request):
    template = loader.get_template('index.html')
    books_count = Book.objects.all().count()
    biblio_data = {"title": "мою библиотеку", "books_count": books_count}
    return HttpResponse(template.render(biblio_data))