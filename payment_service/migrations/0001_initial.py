# Generated by Django 4.1.5 on 2023-01-18 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("borrowings_service", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Status",
                    models.CharField(
                        choices=[("PENDING", "Pending"), ("PAID", "Paid")],
                        max_length=50,
                    ),
                ),
                (
                    "Type",
                    models.CharField(
                        choices=[("PAYMENT", "Payment"), ("FINE", "Fine")],
                        max_length=50,
                    ),
                ),
                ("Session_url", models.URLField(max_length=255)),
                ("Session_id", models.CharField(max_length=50)),
                ("Money_to_pay", models.DecimalField(decimal_places=4, max_digits=19)),
                (
                    "Borrowing_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="borrowings_service.borrowing",
                    ),
                ),
            ],
            options={
                "ordering": ("Status",),
            },
        ),
    ]
