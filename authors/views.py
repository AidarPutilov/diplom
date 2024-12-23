from rest_framework import viewsets

from authors.models import Author
from authors.serializers import AuthorDetailSerializer, AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get_serializer_class(self):
        """Выбор сериализатора в зависимости от запроса."""
        if self.action == "retrieve":
            return AuthorDetailSerializer
        return AuthorSerializer

    def perform_create(self, serializer):
        """Назначение владельца записи."""
        author = serializer.save()
        author.owner = self.request.user
        author.save()
