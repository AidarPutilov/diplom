from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


from authors.serializers import AuthorSerializer
from books.models import Book, Lending


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


class LendingSerializer(serializers.ModelSerializer):
    """Сериализатор для Lending."""

    class Meta:
        model = Lending
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Lending.objects.all(),
                fields=["user", "book"],
                message="Книга выдана"
            )
        ]
