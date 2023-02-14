from django.db import transaction
from rest_framework import serializers
from rest_framework.templatetags.rest_framework import data

from books.models import Book
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
        book = Book.objects.get(data["book"])
        if not book.inventory:
            raise serializers.ValidationError("Inventory is empty, choose another book")
        return data

    def create(self, validated_data):
        book = Book.objects.get(validated_data["book"])
        book.inventory -= 1
        validated_data.self.is_active = True
        self.user_id.id = validated_data["user.id"]  # not sure
        with transaction.atomic():
            book.save()
            self.save()
            instance = super().create(validated_data)
        return instance


class BorrowingReturnSerializer(BorrowingCreateSerializer):
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

    def validate(self, attrs):
        borrowing = Borrowing.objects.get(data["is_active"])
        if not borrowing.self.is_active:
            raise serializers.ValidationError("You have no borrowings")
        return data

    # def update(self, instance, validated_data): Скорее всего тут нужно переопределить метод апдейт
    #    и при вызове этого эндпоинта менять актуал боров ретёрн на боров дейт(актуальная дата), is active менять на False,
    #    а в юзер айди присваивать айди актуального юзера

    def create(self, validated_data):
        book = Book.objects.get(validated_data["book"])
        book.inventory += 1
        validated_data.self.is_active = False
        borrow = Borrowing.objects.get(validated_data["borrowings"])
        borrow.actual_return_date = borrow.borrow_date
        self.user_id.id = validated_data["user.id"]
        with transaction.atomic():
            book.save()
            borrow.save()
            self.save()
            instance = super().create(validated_data)
        return instance
