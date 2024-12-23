from rest_framework import serializers

from authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    """Сериализатор для Author."""

    class Meta:
        model = Author
        fields = ("id", "name")


class AuthorDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для Author RETRIEVE."""

    class Meta:
        model = Author
        fields = "__all__"
