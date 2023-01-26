from django.db import models

from borrowings.models import Borrowing


class Payment(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "PENDING",
        PAID = "PAID"

    class TypeChoices(models.TextChoices):
        PAYMENT = "PAYMENT",
        FINE = "FINE"

    Status = models.CharField(max_length=50, choices=StatusChoices.choices)
    Type = models.CharField(max_length=50, choices=TypeChoices.choices)
    Borrowing_id = models.ForeignKey(Borrowing, on_delete=models.CASCADE)
    Session_url = models.URLField(max_length=255)
    Session_id = models.CharField(max_length=50)
    Money_to_pay = models.DecimalField(max_digits=19, decimal_places=4)

    class Meta:
        ordering = ("Status",)

    def __str__(self):
        return (
            f"{self.Status}"
            f" {self.Type}"
            f" {self.Borrowing_id}"
            f" {self.Session_url}"
            f" {self.Session_id}"
            f" {self.Money_to_pay}"
        )
