from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render

from books.models import Book
from books.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


def index(request):
    """View function for the home page of the site."""

    books = Book.objects.all()

    context = {
        "books": books,
    }

    return render(request, "books/index.html", context=context)
