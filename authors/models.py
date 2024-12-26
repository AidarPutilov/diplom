from django.db import models

from config.settings import AUTH_USER_MODEL


class Author(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="имя автора",
    )
    description = models.CharField(
        max_length=200,
        verbose_name="описание автора",
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
        verbose_name = "автор"
        verbose_name_plural = "авторы"
        ordering = ("name",)

    def __str__(self):
        return self.name
