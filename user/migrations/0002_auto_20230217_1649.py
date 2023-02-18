# Generated by Django 4.1.5 on 2023-02-17 14:49

from django.db import migrations


def generate_superuser(apps, schema_editor):
    """Create a new superuser """
    from django.contrib.auth import get_user_model

    superuser = get_user_model().objects.create_superuser(
        email="max@admin.com",
        password="123",
    )
    superuser.save()


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(generate_superuser),
    ]
