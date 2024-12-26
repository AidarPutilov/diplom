from rest_framework import serializers

# from rest_framework.validators import UniqueTogetherValidator

from authors.serializers import AuthorSerializer
from books.models import Book, Lending


class BookSerializer(serializers.ModelSerializer):
    """Сериализатор для Book."""
    lending = serializers.SerializerMethodField(read_only=True)

    def get_lending(self, book):
        """Возвращает абонента, взявшего книгу."""
        user = self.context["request"].user
        if Lending.objects.all().filter(user=user).filter(book=book).exists():
            return user.name
        return None

    class Meta:
        model = Book
        fields = "__all__"


class BookDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для Book RETRIEVE."""
    authors = AuthorSerializer(many=True, read_only=True, source="author")

    class Meta:
        model = Book
        fields = ("id", "title", "description", "authors", "genre", "owner")


class LendingSerializer(serializers.ModelSerializer):
    """Сериализатор для Lending."""

    class Meta:
        model = Lending
        fields = "__all__"
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Lending.objects.all(),
        #         fields=["user", "book"],
        #         message="Книга выдана"
        #     )
        # ]
