from django.db import models

from borrowings.models import Borrowing


class Payment(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "PENDING",
        PAID = "PAID"

    class TypeChoices(models.TextChoices):
        PAYMENT = "PAYMENT",
        FINE = "FINE"

    status = models.CharField(max_length=50, choices=StatusChoices.choices)
    type = models.CharField(max_length=50, choices=TypeChoices.choices)
    borrowing = models.ForeignKey(Borrowing, on_delete=models.CASCADE)
    session_url = models.URLField(max_length=255)
    session_id = models.CharField(max_length=50)
    money_to_pay = models.DecimalField(max_digits=19, decimal_places=4)

    class Meta:
        ordering = ("status",)

    def __str__(self):
        return (
            f"{self.status}"
            f" {self.type}"
            f" {self.borrowing_id}"
            f" {self.session_url}"
            f" {self.session_id}"
            f" {self.money_to_pay}"
        )
