from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "Title", "Author", "Cover", "Inventory", "Daily_fee")


