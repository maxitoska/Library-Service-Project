from datetime import date

import requests
from django.db import transaction
from rest_framework import serializers

from books.serializers import BookSerializer
from borrowings.models import Borrowing
from user.serializers import UserSerializer
from library_service_project_api.settings import TOKEN, chat_id


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
    TOKEN = TOKEN
    chat_id = chat_id

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

    def expected_money_to_pay(self, attrs):
        book = attrs["book"]
        if date.today().month == attrs["expected_return_date"].month:
            return attrs["expected_return_date"].day - date.today().day * book.daily_fee

    def telegram_notification(self, attrs):
        money_to_pay = self.expected_money_to_pay(attrs)
        message = f"New Borrowing was created. Detail Information:\n" \
                  f"today date: {date.today()}\n" \
                  f"expected return date: {attrs['expected_return_date']}\n" \
                  f"book info: {attrs['book']}\n" \
                  f"expected money to pay: {money_to_pay}$\n" \
                  f"User email: {attrs['user']}"

        url = f"https://api.telegram.org/bot{self.TOKEN}/sendMessage?chat_id={self.chat_id}&text={message}"
        requests.get(url).json()  # this sends the message

    def create(self, validated_data):
        book = validated_data["book"]
        book.inventory -= 1
        with transaction.atomic():
            book.save()
            instance = super().create(validated_data)
            self.expected_money_to_pay(attrs=validated_data)
            self.telegram_notification(attrs=validated_data)
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
        if instance.actual_return_date is None:
            book = instance.book
            book.inventory += 1
            instance.actual_return_date = date.today()
            with transaction.atomic():
                book.save()
                instance.save()
            return instance
        raise serializers.ValidationError("You cannot return borrowing twice")
