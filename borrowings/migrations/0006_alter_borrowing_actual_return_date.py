# Generated by Django 4.1.5 on 2023-02-13 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("borrowings", "0005_alter_borrowing_actual_return_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowing",
            name="actual_return_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
