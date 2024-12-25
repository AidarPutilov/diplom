from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import filters
from books.serializers import BookDetailSerializer, BookSerializer, LendingSerializer

from books.models import Book, Lending


class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        """Назначение владельца записи."""
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "author__name", "genre"]


class BookRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


class BookDestroyAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BooknUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class LendingAPIView(APIView):
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
            message = "Выдача удалена"
        else:
            # Создание выдачи
            Lending.objects.create(user=user, book=book)
            message = "Выдача добавлена"
        return Response({"message": message})
