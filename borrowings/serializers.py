from datetime import date

from django.db import transaction
from rest_framework import serializers

from books.serializers import BookSerializer
from borrowings.models import Borrowing
from user.serializers import UserSerializer


class BorrowingSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "actual_return_date",
            "expected_return_date",
            "user",
            "book",
            "user_id",
            "is_active",
        )


class BorrowingListSerializer(BorrowingSerializer):
    book = BookSerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "actual_return_date",
            "expected_return_date",
            "user",
            "book",
        )


class BorrowingDetailSerializer(BorrowingListSerializer):
    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book",
        )


class BorrowingCreateSerializer(BorrowingSerializer):
    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book",
            "user",
        )

    def validate(self, attrs):
        book = attrs["book"]
        if not book.inventory:
            raise serializers.ValidationError("Inventory is empty, choose another book")
        return attrs

    def create(self, validated_data):
        book = validated_data["book"]
        book.inventory -= 1
        with transaction.atomic():
            book.save()

            instance = super().create(validated_data)
        return instance


class BorrowingReturnSerializer(serializers.Serializer):
    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book",
            "is_active"
        )

    def update(self, instance, validated_data):
        book = instance.book
        book.inventory += 1
        instance.actual_return_date = date.today()
        with transaction.atomic():
            book.save()
            instance.save()
        return instance
