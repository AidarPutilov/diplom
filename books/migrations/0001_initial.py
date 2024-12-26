# Generated by Django 5.1.4 on 2024-12-22 17:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("authors", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=50, verbose_name="название")),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="описание"
                    ),
                ),
                (
                    "genre",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="жанр"
                    ),
                ),
                (
                    "author",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="books_author",
                        to="authors.author",
                        verbose_name="автор",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="владелец записи",
                    ),
                ),
            ],
            options={
                "verbose_name": "книга",
                "verbose_name_plural": "книги",
                "ordering": ("title",),
            },
        ),
    ]
