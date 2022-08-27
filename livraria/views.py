from django.shortcuts import render
from util.livraria.factory import make_book


# Create your views here.
def home(request):
    return render(request, 'livraria/pages/home.html', context={
        'books': [make_book() for _ in range(10)],
    })


def books(request, id):
    return render(request, 'livraria/pages/books.html', context={
        'book': make_book(),
        'is_detail_page': True,
    })
