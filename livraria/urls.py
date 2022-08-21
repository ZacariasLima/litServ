from django.urls import path

from livraria.views import home

urlpatterns = [
    path('', home),
]
