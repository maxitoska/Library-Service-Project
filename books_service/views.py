from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from books_service.models import Book
from books_service.permissions import IsAdminOrIfAuthenticatedReadOnly
from books_service.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

