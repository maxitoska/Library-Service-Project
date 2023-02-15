from django.db import models


class Book(models.Model):
    class CoverChoices(models.TextChoices):
        HARD = "HARD"
        SOFT = "SOFT"

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.CharField(max_length=50, choices=CoverChoices.choices)
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return (
            f"{self.title}"
            f" {self.author}"
            f" {self.cover}"
            f" {self.inventory}"
            f" {self.daily_fee}$"
        )
