from rest_framework import serializers

from authors.serializers import AuthorSerializer
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    """Сериализатор для Book."""

    class Meta:
        model = Book
        fields = "__all__"


class BookDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для Book RETRIEVE."""
    authors = AuthorSerializer(many=True, read_only=True, source="author")

    class Meta:
        model = Book
        # fields = "__all__"
        fields = ("id", "title", "description", "authors", "genre", "owner")
