from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from decimal import Decimal

BOOK_URL = reverse("books:book-list")

DATA = {
    "title": "test_title",
    "author": "test_author",
    "cover": "HARD",
    "inventory": 5,
    "daily_fee": Decimal(10),
}


class AuthorizeBookViewTest(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test@test.com", "testpass", is_staff=False
        )
        self.client.force_authenticate(self.user)

    def test_non_admin_post_request(self) -> None:
        response = self.client.post(BOOK_URL, data=DATA)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class AnonBookViewTest(APITestCase):

    def test_anon_post_request(self) -> None:
        response = self.client.post(BOOK_URL, data=DATA)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AdminBookViewTest(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test1@test.com", "testpass1", is_staff=True, is_superuser=True
        )
        self.client.force_authenticate(self.user)

    def test_admin_post_request(self) -> None:
        response = self.client.post(BOOK_URL, data=DATA)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
