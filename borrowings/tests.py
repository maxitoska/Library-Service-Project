from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from decimal import Decimal
from books.models import Book
from borrowings.models import Borrowing
from user.models import User

BORROW_URL = reverse("borrowings:borrowing-list")


def create_book() -> Book:
    data = {
        "title": "test_title",
        "author": "test_author",
        "cover": "HARD",
        "inventory": 5,
        "daily_fee": Decimal(10),
    }
    return Book.objects.create(**data)


def create_borrowing(book: Book, user: User) -> Borrowing:
    data = {
        "expected_return_date": "2023-02-20",
        "book": book,
        "user": user,
    }
    return Borrowing.objects.create(**data)


class AnonTestBorrowView(APITestCase):
    def test_list_view(self):
        response = self.client.get(BORROW_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class BorrowCreateTest(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test@test.com", "testpass", is_staff=False
        )
        self.client.force_authenticate(self.user)

    def test_book_inventory(self) -> None:
        book = create_book()
        create_data = {
            "expected_return_date": "2023-02-20",
            "book": book.id,
            "user": self.user.id,
        }
        response = self.client.post(BORROW_URL, data=create_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        book = Book.objects.get(id=book.id)
        self.assertEqual(book.inventory, 4)

    def test_return_book(self) -> None:
        book = create_book()
        borrowing = create_borrowing(book, self.user)
        borrow_url_return = reverse(
            "borrowings:borrowing-return-book",
            kwargs={"pk": borrowing.id}
        )
        response = self.client.patch(borrow_url_return)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book = Book.objects.get(id=book.id)
        self.assertEqual(book.inventory, 6)
