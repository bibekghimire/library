from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views



urlpatterns=[
    path("book/", views.book_list, name='book_list'),
    path("borrows/", views.borrowed_books, name='borrowed_books'),
]
