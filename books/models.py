from django.db import models

from authors.models import Author
from config.settings import AUTH_USER_MODEL


class Book(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="название",
    )
    description = models.CharField(
        max_length=200,
        verbose_name="описание",
        null=True,
        blank=True,
    )
    author = models.ManyToManyField(
        Author,
        verbose_name="автор",
        related_name="books_author",
        null=True,
        blank=True,
    )
    genre = models.CharField(
        max_length=200,
        verbose_name="жанр",
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="владелец записи",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"
        ordering = ("title",)

    def __str__(self):
        return self.title
