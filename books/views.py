from books.serializers import BookDetailSerializer, BookSerializer
from rest_framework import viewsets

from books.models import Book


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_serializer_class(self):
        """Выбор сериализатора в зависимости от запроса."""
        if self.action == "retrieve":
            return BookDetailSerializer
        return BookSerializer

    def perform_create(self, serializer):
        """Назначение владельца записи."""
        book = serializer.save()
        book.owner = self.request.user
        book.save()

    # def perform_update(self, serializer):
    #     """Оправка писем при обновлении курса."""
    #     # print("1")
    #     course = serializer.save()
    #     # print("2")
    #     course_pk = self.get_object().pk
    #     send_info.delay(course_pk)
    #     course.save()

    # def get_permissions(self):
    #     """Назначение разрешений."""
    #     if self.action == "create":
    #         self.permission_classes = (~IsModer,)
    #     elif self.action == "destroy":
    #         self.permission_classes = (~IsModer | IsOwner,)
    #     elif self.action in ["update", "retrieve"]:
    #         self.permission_classes = (IsModer | IsOwner,)
    #     return super().get_permissions()
