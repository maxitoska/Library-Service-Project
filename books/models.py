from django.db import models


class Book(models.Model):
    class CoverChoices(models.TextChoices):
        HARD = "HARD"
        SOFT = "SOFT"

    Title = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    Cover = models.CharField(max_length=50, choices=CoverChoices.choices)
    Inventory = models.PositiveIntegerField()
    Daily_fee = models.DecimalField(max_digits=19, decimal_places=4)

    class Meta:
        ordering = ("Title",)

    def __str__(self):
        return (
            f"{self.Title}"
            f" {self.Author}"
            f" {self.Cover}"
            f" {self.Inventory}"
            f" {self.Daily_fee}$"
        )
