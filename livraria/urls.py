from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('books/<int:id>/', views.books),

]
