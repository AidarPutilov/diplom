from django.urls import path
from books.views import (
    BookCreateAPIView,
    BookDestroyAPIView,
    BookListAPIView,
    BookRetrieveAPIView,
    BooknUpdateAPIView,
    LendingAPIView,
)
from books.apps import BooksConfig


app_name = BooksConfig.name

urlpatterns = [
    path("list/", BookListAPIView.as_view(), name="book_list"),
    path("detail/<int:pk>/", BookRetrieveAPIView.as_view(), name="book_retrieve"),
    path("create/", BookCreateAPIView.as_view(), name="book_create"),
    path("delete/<int:pk>/", BookDestroyAPIView.as_view(), name="book_delete"),
    path("update/<int:pk>/", BooknUpdateAPIView.as_view(), name="book_update"),
    path("lending/", LendingAPIView.as_view(), name="lending"),
]
