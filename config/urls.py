from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("author/", include("authors.urls", namespace="author")),
    path("book/", include("books.urls", namespace="book")),
]
