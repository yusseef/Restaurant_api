# Generated by Django 4.1.7 on 2023-03-29 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Restaurant",
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
                    "name",
                    models.CharField(
                        help_text="Required | max-100",
                        max_length=100,
                        verbose_name="Restaurant name",
                    ),
                ),
                (
                    "address",
                    models.TextField(
                        help_text="Required | max-500",
                        max_length=500,
                        verbose_name="Restaurant address",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        help_text="Required | max-100",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="restaurants",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Restaurant owner",
                    ),
                ),
            ],
        ),
    ]