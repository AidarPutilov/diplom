from rest_framework import viewsets

from authors.models import Author
from authors.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def perform_create(self, serializer):
        """Назначение владельца записи."""
        course = serializer.save()
        course.owner = self.request.user
        course.save()
