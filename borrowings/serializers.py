from django.db import transaction
from rest_framework import serializers
from rest_framework.templatetags.rest_framework import data

from books.models import Book
from books.serializers import BookSerializer
from borrowings.models import Borrowing
from user.serializers import UserSerializer


class BorrowingSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=False)
    user_id = serializers.IntegerField()

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book_id",
            "user_id",
            "is_active"
        )

    def validate(self, attrs):
        book = Book.objects.get(data["book_id"])
        if not book.inventory:
            raise serializers.ValidationError("Inventory is empty, choose another book")
        return data

    def create(self, validated_data):
        book = Book.objects.get(validated_data["book_id"])
        book.inventory -= 1
        self.is_active = True
        self.user_id = book.id  # not sure
        with transaction.atomic():
            book.save()
            instance = super().create(validated_data)
        return instance


class BorrowingListSerializer(BorrowingSerializer):
    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book_id",

        )


class BorrowingDetailSerializer(BorrowingSerializer):
    book_id = BookSerializer(many=False, read_only=True)
    user_id = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book_id",

        )


class BorrowingReturnSerializer(BorrowingSerializer):
    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book_id",
            "is_active"
        )

    def validate(self, attrs):
        borrowing = Borrowing.objects.get(data["is_active"])
        if not borrowing.is_active:
            raise serializers.ValidationError("You have no borrowings")
        return data

    def create(self, validated_data):
        book = Book.objects.get(validated_data["book_id"])
        book.inventory += 1
        self.is_active = False
        self.user_id = id  # not sure
        with transaction.atomic():
            book.save()
            instance = super().create(validated_data)
        return instance
