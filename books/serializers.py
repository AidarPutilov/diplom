from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    """Сериализатор для Book."""

    class Meta:
        model = Book
        fields = "__all__"
