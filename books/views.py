from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import filters
from books.serializers import (
    BookDetailSerializer,
    BookSerializer,
    LendingSerializer
)

from books.models import Book, Lending


class BookCreateAPIView(generics.CreateAPIView):
    """API CREATE для книги."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        """Назначение владельца записи."""
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class BookListAPIView(generics.ListAPIView):
    """API GET для книги."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "author__name", "genre"]


class BookRetrieveAPIView(generics.RetrieveAPIView):
    """API RETRIVE для книги."""
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


class BookDestroyAPIView(generics.DestroyAPIView):
    """API DELETE для книги."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BooknUpdateAPIView(generics.UpdateAPIView):
    """API PATCH для книги."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class LendingAPIView(APIView):
    """API GET для выдачи книги. Вызов добавляет запись,
    повторный вызов - удаляет её."""
    queryset = Lending.objects.all()
    serializer_class = LendingSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        book_id = request.data.get("book")
        book = get_object_or_404(Book, pk=book_id)
        subs_item = Lending.objects.filter(user=user, book=book)

        if subs_item.exists():
            # Удаление выдачи
            subs_item.delete()
            message = "Книга возвращена"
        else:
            # Создание выдачи
            Lending.objects.create(user=user, book=book)
            message = "Книга выдана"
        return Response({"message": message})
