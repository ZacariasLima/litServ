from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'livraria/pages/home.html')


def books(request, id):
    return render(request, 'livraria/pages/books.html')
