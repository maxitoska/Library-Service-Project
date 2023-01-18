from django.conf import settings
from django.db import models

from books_service.models import Book
from user.models import User


class Borrowing(models.Model):
    class CoverChoices(models.TextChoices):
        HARD = "HARD"
        SOFT = "SOFT"

    Borrow_date = models.DateField()
    Expected_return_date = models.DateField()
    Actual_return_date = models.DateField(auto_now_add=True)
    Book_id = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="borrowings"
    )
    User_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("Borrow_date",)

    def __str__(self):
        return (
            f"{self.Borrow_date}"
            f" {self.Expected_return_date}"
            f" {self.Actual_return_date}"
            f" {self.Book_id}"
            f" {self.User_id}"
        )
