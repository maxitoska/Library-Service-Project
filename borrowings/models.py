from django.conf import settings
from django.db import models

from books.models import Book
from user.models import User


class Borrowing(models.Model):
    class CoverChoices(models.TextChoices):
        HARD = "HARD"
        SOFT = "SOFT"

    is_active = models.BooleanField(default=False)
    borrow_date = models.DateField()
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(auto_now_add=True)
    book_id = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="borrowings"
    )
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="borrowings"
    )

    class Meta:
        ordering = ("borrow_date",)

    def str(self):
        return (
            f"{self.borrow_date}"
            f" {self.expected_return_date}"
            f" {self.actual_return_date}"
            f" {self.book_id}"
            f" {self.user_id}"
            f" {self.is_active}"
        )
