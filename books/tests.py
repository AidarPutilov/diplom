from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authors.models import Author
from books.models import Book
from users.models import User


class AuthorTestCase(APITestCase):
    """Тестирование модели Author."""

    def setUp(self):
        """Окружение для тестов."""
        self.user = User.objects.create(email="test@sky.pro")
        self.author = Author.objects.create(
            name="Test author",
            description="Test author description",
            owner=self.user,
        )
        # self.book = Book.objects.create(
        #     title="Test book",
        #     description="Test book description",
        #     author=(self.author,),
        #     genre="Test genre",
        #     owner=self.user,
        # )
        self.client.force_authenticate(user=self.user)

    def test_author_retrieve(self):
        """Тестирование Author RETRIVE."""
        url = reverse("author:author-detail", args=(self.author.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.author.name)

    def test_author_create(self):
        """Тестирование Author CREATE."""
        url = reverse("author:author-list")
        data = {
            "name": "Test author 2",
            "description": "Test description 2",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.all().count(), 2)

    def test_author_update(self):
        """Тестирование Author UPDATE"""
        url = reverse("author:author-detail", args=(self.author.pk,))
        data = {"name": "Test author new"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Test author new")

    def test_author_delete(self):
        """Тестирование Author DELETE"""
        url = reverse("author:author-detail", args=(self.author.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.all().count(), 0)

    def test_author_list(self):
        """Тестирование Author LIST"""
        url = reverse("author:author-list")
        response = self.client.get(url)
        data = response.json()
        result = [{
            "id": self.author.pk,
            "name": self.author.name,
            # "description": self.author.description,
            # "owner": self.user.pk,
        }]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class BookTestCase(APITestCase):
    """Тестирование модели Book."""

    def setUp(self):
        """Окружение для тестов."""
        self.user = User.objects.create(email="test@sky.pro")
        # self.author = Author.objects.create(
        #     name="Test author",
        #     description="Test author description",
        #     owner=self.user,
        # )
        self.book = Book.objects.create(
            title="Test book",
            description="Test book description",
            # author=(self.author,),
            genre="Test genre",
            owner=self.user,
        )
        self.author = self.book.author.create(name="Test author")
        self.author.save
        self.client.force_authenticate(user=self.user)

    def test_book_retrieve(self):
        """Тестирование Book RETRIVE."""
        url = reverse("book:book_detail", args=(self.book.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.book.title)
        self.assertEqual(data.get("description"), self.book.description)
        self.assertEqual(data.get("genre"), self.book.genre)

    def test_book_create(self):
        """Тестирование Book CREATE."""
        url = reverse("book:book_create")
        data = {
            "title": "Test book 2",
            "description": "Test description 2",
            "genre": "Test genre 2",
        }
        author = self.book.author.create(name="Test author 2")
        author.save()
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.all().count(), 2)

    def test_book_update(self):
        """Тестирование Book UPDATE"""
        url = reverse("book:book_update", args=(self.book.pk,))
        data = {"title": "Test title new"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Test title new")

    def test_book_delete(self):
        """Тестирование Book DELETE"""
        url = reverse("book:book_delete", args=(self.book.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.all().count(), 0)

    def test_book_list(self):
        """Тестирование Book LIST"""
        url = reverse("book:book_list")
        response = self.client.get(url)
        data = response.json()
        result = [{
            "id": self.book.pk,
            "lending": None,
            "title": self.book.title,
            "description": self.book.description,
            "genre": self.book.genre,
            "author": [self.author.pk],
            "owner": self.user.pk,
        }]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
