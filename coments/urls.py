from django.urls import path

from coments.views import home

urlpatterns = [
    path('', home),
]
